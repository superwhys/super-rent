#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main

from database import get_client
from pymongo.database import Database
from curd import get_user, get_unit_rent_by_name

from typing import Optional
from datetime import datetime, timedelta
from schemas import Token, User, UnitRentLst, UserAuthority

from jose import JWTError, jwt
from passlib.context import CryptContext
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

from fastapi.security import OAuth2PasswordBearer
from fastapi import APIRouter, Form, Depends, HTTPException, status

from loguru import logger


app = APIRouter()


def get_db():
    client = get_client('localhost:27017')
    try:
        logger.info('get client')
        yield client['super_rent']
    finally:
        client.close()
        logger.info('client close')


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/rent/login")


def verify_password(plain_password: str, hashed_password: str):
    """
    verify the password which the user input with the password in database
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def authenticate_user(username: str, password: str, db: Database):
    """
    get the user from database and verify the password
    :param db:
    :param username:
    :param password:
    :return: user
    """
    _user = get_user(db, username)
    logger.info(f'_user is : {_user}')
    user = User(**_user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: Optional[dict] = None,
                        old_token: Optional[str] = None,
                        expires_delta: Optional[timedelta] = None):
    """
    create token after certification
    :param old_token:
    :param data:
    :param expires_delta:
    :return:
    """

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=30)
    # create new token
    if old_token is None:
        # time out
        to_encode = data.copy()
        to_encode.update({"exp": expire})
        token = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    else:
        logger.info('has old token')
        to_encode = jwt.decode(token=old_token, key=SECRET_KEY, algorithms=[ALGORITHM])
        old_token_date = to_encode.get('create_time')
        old_token_date = datetime.strptime(old_token_date, "%Y-%m-%d %H:%M:%S")
        # if the time interval is 20 minutes, update the token
        if (datetime.now() - old_token_date).seconds > 1200:
            logger.info('update old token')
            to_encode['create_time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            to_encode.update({"exp": expire})
            token = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
        else:
            # not time out
            token = old_token
    return token


@app.post("/login", response_model=Token)
async def login(username: str = Form(...), password: str = Form(...), db: Database = Depends(get_db)):
    """
    :param db:
    :param username:
    :param password:
    :return:
    """
    user = authenticate_user(username, password, db)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # token expire time
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    access_token = create_access_token(
        data={'sub': user.user_name, 'auth': user.authority, 'create_time': now_time},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token,
            'token_type': 'bearer'}


@app.options("/get_unit_rent")
async def get_unit_rent(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    return True


@app.get("/get_unit_rent")
async def get_unit_rent(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    Get the unit rent under the current account authority name
    if account is contractor, it just show the unit rent it has
    if account is owner, it will show all the unit rent it has
    :param db:
    :param token:
    :return:
    """
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # get the username and authority in token
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username is None:
            raise credentials_exception

        authority = token_decode.get('auth')
    except JWTError:
        raise credentials_exception

    # get different information according to different authority
    unit_rent_lst = {}
    if authority == UserAuthority.owner:
        unit_rent = get_unit_rent_by_name(db, rent_owner=username)
        unit_rent_lst = {'rent_owner': username, 'unit_rent_lst': unit_rent}
    if authority == UserAuthority.contractor:
        unit_rent = get_unit_rent_by_name(db, rent_admin=username)
        unit_rent_lst = {'rent_admin': username, 'unit_rent_lst': unit_rent}
    logger.info(f'get_unit_rent_by_name: {username}, {unit_rent_lst}')
    return UnitRentLst(**unit_rent_lst)
