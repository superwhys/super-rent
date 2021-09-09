#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : general_module.py
# @Author: SuperYong
# @Date  : 2021/9/58:46 下午
# @Desc  :

from loguru import logger
from typing import Optional
from pymongo.database import Database
from datetime import datetime, timedelta

from common.curd import get_user
from common.schemas import User
from config import SECRET_KEY, ALGORITHM, pwd_context, credentials_exception

from jose import jwt, JWTError
from fastapi import Request, HTTPException, status


def verify_password(plain_password: str, hashed_password: str):
    """
    verify the password which the user input with the password in database
    :param plain_password:
    :param hashed_password:
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_user_name_in_token(token):
    """
    :param token:
    :return:
    """
    # get the username and authority in token
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username is None:
            raise credentials_exception
        authority = token_decode.get('auth')
    except JWTError:
        raise credentials_exception
    else:
        return username, authority


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


async def get_user_agent(request: Request):
    """
    get token from user agent, Authorization
    judge the token in user agent
    :param request:
    :return:
    """
    logger.info('in this')
    token = request.headers.get('Authorization')
    if not token:
        raise HTTPException(
            status_code=status.HTTP_407_PROXY_AUTHENTICATION_REQUIRED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
