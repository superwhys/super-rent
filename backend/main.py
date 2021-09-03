#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main

import uvicorn
from jose import JWTError, jwt
from pymongo import MongoClient
from typing import List, Optional
from passlib.context import CryptContext
from datetime import datetime, timedelta
from database import get_client, get_table
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from fastapi import APIRouter, Form, Depends, HTTPException, BackgroundTasks, status

from schemas import Token, User
from curd import get_user


app = APIRouter()


def get_db():
    client = get_client('localhost:27017')
    try:
        yield client['super_rent']
    finally:
        client.close()


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


def authenticate_user(username: str, password: str, client: MongoClient):
    """
    get the user from database and verify the password
    :param username:
    :param password:
    :param client:
    :return: user
    """
    db = client['super_rent']
    _user = get_user(db, username)
    user = User(**_user)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    create token after certification
    :param data:
    :param expires_delta:
    :return:
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(claims=to_encode, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login", response_model=Token)
async def login(username: str = Form(...), password: str = Form(...)):
    """
    :param username:
    :param password:
    :return:
    """
    # async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    client = get_client("localhost:27017")
    user = authenticate_user(username, password, client)
    # user = authenticate_user(form_data.username, form_data.password, client)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # token expire time
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={'sub': user.user_name},
        expires_delta=access_token_expires
    )
    return {'access_token': access_token,
            'token_type': 'bearer'}
