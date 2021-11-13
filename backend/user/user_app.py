#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/58:41 下午
# @Desc  :


from common.database import get_db
from common.curd import get_user, create_user
from common.schemas import Token, RegisterStatus, User
from common.general_module import create_access_token, authenticate_user

from descriptions import login_desc, register_desc
from config import ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context

from time import time
from loguru import logger
from pymongo.database import Database
from base64 import b64encode, b64decode
from datetime import datetime, timedelta
from fastapi import APIRouter, Form, Depends, HTTPException, status

user_app = APIRouter()


@user_app.post("/user/login", response_model=Token,
               summary='登录',
               description=login_desc)
async def login(account_id: str = Form(...), password: str = Form(...), db: Database = Depends(get_db)):
    """
    :param db:
    :param account_id:
    :param password: base64(timestamp-md5(pwd))
    :return:
    """
    password_decode = b64decode(password.encode('utf-8')).decode('utf-8')
    pwd_b64decode_split = password_decode.split('-')

    pwd_cipher = pwd_b64decode_split[1]
    timestamp = int(pwd_b64decode_split[0] + pwd_b64decode_split[2])
    now_stamp = int(time())

    logger.info(f'{timestamp} - {pwd_cipher}')

    if now_stamp - timestamp > 1800:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="this visit has timeout!",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = authenticate_user(account_id, pwd_cipher, db)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect account_id or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # token expire time
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    access_token = create_access_token(
        data={'sub': user.account_id, 'auth': user.authority, 'create_time': now_time},
        expires_delta=access_token_expires
    )
    return {'status': True, 'token': {'access_token': access_token,
                                      'token_type': 'bearer'}}


@user_app.post("/user", response_model=RegisterStatus,
               summary='注册',
               description=register_desc)
async def register(user: User, db: Database = Depends(get_db)):
    """
    :param user: password: base64(timestamp-md5(pwd))
    :param db:
    :return:
    """
    if get_user(db, user.account_id):
        return {'status': False, 'msg': 'this username has been register'}

    pwd_cipher = user.password.encode('utf-8')
    pwd_b64decode = b64decode(pwd_cipher).decode('utf-8')
    pwd_b64decode_split = pwd_b64decode.split('-')
    pwd = pwd_b64decode_split[1]

    timestamp = int(pwd_b64decode_split[0] + pwd_b64decode_split[2])
    now_stamp = int(time())

    logger.info(f'{timestamp} - {pwd}')

    if now_stamp - timestamp > 1800:
        return {'status': False, 'msg': 'this visit has timeout!'}

    user.password = pwd_context.hash(pwd)
    if create_user(db, user):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        access_token = create_access_token(
            data={'sub': user.account_id, 'auth': user.authority, 'create_time': now_time},
            expires_delta=access_token_expires
        )
        return {'status': True, 'token': {'access_token': access_token,
                                          'token_type': 'bearer'}}
    else:
        return {'status': False, 'msg': 'Interface exception'}
