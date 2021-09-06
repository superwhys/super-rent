#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : tenant_app.py
# @Author: SuperYong
# @Date  : 2021/9/610:36 下午
# @Desc  :

from config import oauth2_schema
from descriptions import create_tenant_desc

from common.database import get_db
from common.general_module import get_user_agent
from common.schemas import Tenant, Token

from fastapi import APIRouter, Depends
from pymongo.database import Database


tenant_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@tenant_app.post("/create_tenant",
                 summary="创建一个租客",
                 description=create_tenant_desc)
async def create_tenant(tenant: Tenant, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param db:
    :param tenant:
    :param token:
    :return:
    """
    pass


