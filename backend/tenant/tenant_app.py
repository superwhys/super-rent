#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tenant_app.py
# @Author: SuperYong
# @Date  : 2021/9/610:36 下午
# @Desc  :

from config import oauth2_schema
from descriptions import create_tenant_desc, get_tenant_info_desc

from common.database import get_db
from common.schemas import Tenant, Token
from common.general_module import get_user_agent, get_user_name_in_token
from common.curd import get_tenant, create_tenant

from pymongo.database import Database
from fastapi import APIRouter, Depends, HTTPException, status

tenant_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@tenant_app.post("/create_tenant",
                 summary="创建一个租客",
                 description=create_tenant_desc)
async def create_tenant_api(tenant: Tenant, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param db:
    :param tenant:
    :param token:
    :return:
    """
    if not tenant.name or not tenant.id_card:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Tenant name or id card is None",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user, authority = get_user_name_in_token(token)
    if authority not in ['admin', 'owner', 'contractor']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permissions",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if get_tenant(db, tenant.name, tenant.id_card) is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The tenant already exists",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if create_tenant(db, tenant):
        return {'status': 'Success', 'msg': "create success"}
    return {'status': False, 'msg': 'create tenant error, retry'}


@tenant_app.get("/get_tenant_into",
                summary="获取租客信息",
                deprecated=True,
                description=get_tenant_info_desc)
async def get_tenant_info(name: str, unit_rent: str, rent_room: str,
                          db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param db:
    :param name:
    :param unit_rent:
    :param rent_room:
    :param token:
    :return:
    """
    user, authority = get_user_name_in_token(token)
    if authority not in ['admin', 'owner', 'contractor']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permissions",
            headers={"WWW-Authenticate": "Bearer"}
        )
    pass
