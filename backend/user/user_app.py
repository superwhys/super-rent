#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/58:41 下午
# @Desc  :

from common.database import get_db
from pymongo.database import Database
from datetime import datetime, timedelta

from common.curd import get_user, create_user
from common.schemas import Token, RegisterStatus, User
from common.general_module import create_access_token, authenticate_user

from config import ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context

from fastapi import APIRouter, Form, Depends, HTTPException, status


user_app = APIRouter()


@user_app.post("/login", response_model=Token,
               summary='登录')
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


@user_app.post("/register", response_model=RegisterStatus,
               summary='注册')
async def register(user: User, db: Database = Depends(get_db)):
    """
    :param user:
    :param db:
    :return:
    """
    if get_user(db, user.user_name):
        return {'status': False, 'msg': 'this username has been register'}
    user.password = pwd_context.hash(user.password)
    if create_user(db, user):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        access_token = create_access_token(
            data={'sub': user.user_name, 'auth': user.authority, 'create_time': now_time},
            expires_delta=access_token_expires
        )
        return {'status': True, 'token': {'access_token': access_token,
                                          'token_type': 'bearer'}}
    else:
        return {'status': False, 'msg': 'Interface exception'}
