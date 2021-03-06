#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tenant_app.py
# @Author: SuperYong
# @Date  : 2021/9/610:36 下午
# @Desc  :

from config import oauth2_schema, credentials_exception
from descriptions import create_tenant_desc, get_tenant_info_desc

from common.database import get_db
from common.schemas import Tenant, BaseToken, TenantInfoRes, RequestStatus
from common.general_module import get_user_agent, get_account_in_token
from common.curd import get_tenant, create_tenant

from pymongo.database import Database
from fastapi import APIRouter, Depends, HTTPException, status

tenant_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@tenant_app.post("/tenant",
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
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tenant name or id card is None",
            headers={"WWW-Authenticate": "Bearer"},
        )

    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception

    if authority not in ['admin', 'owner', 'contractor']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permissions",
            headers={"WWW-Authenticate": "Bearer"}
        )
    if get_tenant(db, tenant.name, tenant.id_card) is not None:
        raise HTTPException(
            status_code=status.HTTP_200_OK,
            detail="The tenant already exists",
            headers={"WWW-Authenticate": "Bearer"}
        )

    if create_tenant(db, tenant):
        return {'status': 'Success', 'msg': "create success"}
    return {'status': False, 'msg': 'create tenant error, retry'}


@tenant_app.get("/tenant",
                summary="获取租客信息",
                response_model=TenantInfoRes,
                description=get_tenant_info_desc)
async def get_tenant_info(name: str, id_card: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param db:
    :param name:
    :param id_card:
    :param token:
    :return:
    """
    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception

    if authority not in ['admin', 'owner', 'contractor']:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient permissions",
            headers={"WWW-Authenticate": "Bearer"}
        )
    tenant = get_tenant(db, name, id_card)
    tenant_res = {'status': RequestStatus.success, 'tenant': tenant}
    return TenantInfoRes(**tenant_res)
