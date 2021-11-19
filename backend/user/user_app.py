#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/58:41 下午
# @Desc  :

from common.database import get_db
from common.common_utils import get_encrypt_decode
from common.curd import get_user, create_user, get_auth_code, get_user_rent_info_data
from common.schemas import LoginRes, User, RegisterStatus, RequestStatus, UserAuthority, UserRentInfo
from common.general_module import create_access_token, authenticate_user, get_account_in_token

from descriptions import login_desc, register_desc
from config import ACCESS_TOKEN_EXPIRE_MINUTES, AUTH_CODE, pwd_context, oauth2_schema, credentials_exception

from time import time
from loguru import logger
from base64 import b64decode
from pymongo.database import Database
from datetime import datetime, timedelta
from fastapi import APIRouter, Form, Depends, HTTPException, status

user_app = APIRouter()


@user_app.post("/user/login", response_model=LoginRes,
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
        return {'status': RequestStatus.error, 'msg': "username or password error"}
    # token expire time
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    now_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    access_token = create_access_token(
        data={'sub': user.account_id, 'auth': user.authority, 'create_time': now_time},
        expires_delta=access_token_expires
    )
    return {'status': RequestStatus.success, 'username': user.user_name,
            'access_token': access_token, 'token_type': 'bearer'}


@user_app.post("/user", response_model=RegisterStatus,
               summary='注册',
               description=register_desc)
async def register(user: User, auth_code: str, db: Database = Depends(get_db)):
    """
    :param user: password: base64(timestamp[:5]-md5(pwd)-timestamp[5:])
    :param auth_code: Authorization code base64(timestamp[:5]-md5(name)-md5(AuthCode)-timestamp[5:])
    MTYzNzAtYzcxN2NmYWNmYWY1NGQxYjEwYzE0NmYzMDBhN2ZlMmUtNTMyNzUyYTI4MjYzMGUzMjZlODU5ZTE3ZWM1YzM1MzUtNDQ1NDU=
    :param db:
    :return:
    """
    now_stamp = int(time())
    logger.debug(user)
    try:
        auth_code_split = b64decode(auth_code.encode("utf-8")).decode("utf-8").split('-')
        timestamp = int(auth_code_split[0] + auth_code_split[-1])
        # c717cfacfaf54d1b10c146f300a7fe2e
        auth_code_name = auth_code_split[1]
        auth_code_base = auth_code_split[2]
    except Exception:
        logger.error("auth code error")
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail={'status': RequestStatus.error, 'msg': "Auth code Nonconformity to specification"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    if any((timedelta(seconds=now_stamp - timestamp).days > 7,
            not get_auth_code(db, auth_code_name),
            auth_code_base != AUTH_CODE)):
        raise HTTPException(
            status.HTTP_403_FORBIDDEN,
            detail={'status': RequestStatus.error, 'msg': "this Authorization code is not useful"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    if get_user(db, user.account_id):
        raise HTTPException(
            status.HTTP_200_OK,
            detail={status: RequestStatus.error, 'msg': "this username has been register"},
            headers={"WWW-Authenticate": "Bearer"},
        )

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
    if token_account is None or authority is None:
        raise credentials_exception

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
