#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# @File    ：bill_app.py
# @IDE     ：PyCharm 
# @Author  ：SuperYong
# @Date    ：2021/11/25 17:20 
# @Summary : this is the summary
from common.database import get_db
from pymongo.database import Database
from config import oauth2_schema, ERROR_HEADER, credentials_exception
from common.general_module import get_user_agent, get_account_in_token

from loguru import logger
from fastapi import APIRouter, Depends, HTTPException, status

bill_app = APIRouter(
    # 过滤没有token的请求
    dependencies=[Depends(get_user_agent)]
)

# TODO bill database _id need to use a data that can identify a unique bill_info
# md5()


@bill_app.post("/bill",
               deprecated=True)
async def create_bill(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO create a new bill
    pass


@bill_app.put("/bill",
              deprecated=True)
async def update_bill(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO update a new bill
    pass


@bill_app.get("/bill/{unit_rent}/{unit_room}/{month}",
              deprecated=True)
async def update_bill(unit_rent: str, unit_room: str, month: int,
                      db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO update a new bill
    pass


@bill_app.delete("/bill",
                 deprecated=True)
async def delete_bill(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO delete a new bill
    pass
