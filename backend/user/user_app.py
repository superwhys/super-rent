#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/58:41 下午
# @Desc  :

from common.database import get_db
from common.common_utils import get_encrypt_decode
from common.curd import get_user, create_user, get_auth_code, get_user_rent_info_data
from common.schemas import BaseToken, User, RegisterStatus, RequestStatus, UserAuthority, UserRentInfo
from common.general_module import create_access_token, authenticate_user, get_account_in_token

from descriptions import login_desc, register_desc
from config import ACCESS_TOKEN_EXPIRE_MINUTES, pwd_context, oauth2_schema

from time import time
from loguru import logger
from pymongo.database import Database
from datetime import datetime, timedelta
from fastapi import APIRouter, Form, Depends, HTTPException, status

user_app = APIRouter()


@user_app.post("/user/login", response_model=BaseToken,
               summary='登录',
               description=login_desc)
async def login(username: str = Form(...), password: str = Form(...), db: Database = Depends(get_db)):
    """
    :param db:
    :param username:
    :param password: base64(timestamp-md5(pwd))
    :return:
    """
    account_id = username
    timestamp, pwd_cipher = get_encrypt_decode(password)
    now_stamp = int(time())

    logger.info(f'{timestamp} - {pwd_cipher}')

    if now_stamp - timestamp > 1800:
        raise HTTPException(
            status.HTTP_408_REQUEST_TIMEOUT,
            detail={'status': RequestStatus.error, 'msg': "this visit has timeout!"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = authenticate_user(account_id, pwd_cipher, db)
    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail={'status': RequestStatus.error, 'msg': "Incorrect account_id or password"},
            headers={"WWW-Authenticate": "Bearer"},
        )
    # token expire time
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    access_token = create_access_token(
        data={'sub': user.account_id, 'auth': user.authority, 'create_time': now_time},
        expires_delta=access_token_expires
    )
    return {'status': RequestStatus.success, 'access_token': access_token, 'token_type': 'bearer'}


@user_app.post("/user", response_model=RegisterStatus,
               summary='注册',
               description=register_desc)
async def register(user: User, auth_code: str, db: Database = Depends(get_db)):
    """
    :param user: password: base64(timestamp-md5(pwd))
    :param auth_code: Authorization code
    :param db:
    :return:
    """
    now_stamp = int(time())

    timestamp, _ = get_encrypt_decode(auth_code)
    if timedelta(seconds=now_stamp - timestamp).days > 7 or not get_auth_code(db, auth_code):
        return {'status': RequestStatus.error, 'msg': 'this Authorization code is not useful'}

    if get_user(db, user.account_id):
        return {'status': RequestStatus.error, 'msg': 'this username has been register'}

    timestamp, pwd = get_encrypt_decode(user.password)

    logger.info(f'{timestamp} - {pwd}')

    if now_stamp - timestamp > 1800:
        raise HTTPException(
            status.HTTP_408_REQUEST_TIMEOUT,
            detail={'status': RequestStatus.error, 'msg': "this visit has timeout!"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    user.password = pwd_context.hash(pwd)
    if create_user(db, user):
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        access_token = create_access_token(
            data={'sub': user.account_id, 'auth': user.authority, 'create_time': now_time},
            expires_delta=access_token_expires
        )
        return {'status': RequestStatus.success, 'token': {'access_token': access_token,
                                                           'token_type': 'bearer'}}
    else:
        return {'status': RequestStatus.error, 'msg': 'Interface exception'}


@user_app.get("/user",
              summary="获取用户相关信息",
              description="",
              response_model=UserRentInfo
              )
async def get_user_info(account_id: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    get each unit rental type num and total price
    :param account_id:
    :param token:
    :param db:
    :return:
    """
    token_account, authority = get_account_in_token(token)

    if token_account != account_id:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail={'status': RequestStatus.error, 'msg': "account not allow"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    user_dic = get_user(db, account_id)
    user_info = {'account_id': account_id, 'username': user_dic['user_name']}

    user_rental_info = get_user_rent_info_data(db, account_id, authority)
    user_info.update(user_rental_info)

    user_info['status'] = RequestStatus.success
    return user_info
