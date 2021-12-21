#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# @File    ：bill_app.py
# @IDE     ：PyCharm 
# @Author  ：SuperYong
# @Date    ：2021/11/25 17:20 
# @Summary : this is the summary
from datetime import datetime

from common.curd import get_charges_data, insert_bill_info, get_rent_room, create_bill_info_id, get_specify_bill_info, \
    update_specify_bill_info
from common.database import get_db
from pymongo.database import Database

from common.schemas import BaseBill, BillInfo, RequestStatus
from config import oauth2_schema, ERROR_HEADER, credentials_exception
from common.general_module import get_user_agent, get_account_in_token

from loguru import logger
from fastapi import APIRouter, Depends, HTTPException, status

# TODO add the checker of the unit rental into dependencies
bill_app = APIRouter(
    # filter the request that has no token
    dependencies=[Depends(get_user_agent)]
)

# bill database _id need to use a data that can identify a unique bill_info
# md5(unit_rent-unit_rent_room-year-month)


@bill_app.post("/bill")
async def create_bill(tenant: str, unit_rent: str, unit_rent_room: str,
                      resource_use: BaseBill,
                      db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO check if the unit rental is under this account
    # TODO add to middleware
    token_account, authority = get_account_in_token(token)
    if token_account is None or authority is None:
        raise credentials_exception

    if not tenant or not unit_rent or not unit_rent_room or not resource_use:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'status': RequestStatus.error, 'msg': 'parameter is None'}
        )

    try:
        charge = get_charges_data(db, unit_rent)
        rent_room = get_rent_room(db, unit_rent, unit_rent_room)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail={'status': RequestStatus.error, 'msg': 'Service unreachable'}
        )
    else:
        if charge is None or rent_room is None:
            raise HTTPException(
                status_code=status.HTTP_204_NO_CONTENT,
                detail={'status': RequestStatus.error, 'msg': 'unit rent error'}
            )

    now_time = datetime.now()
    bill_info = {
        'tenant': tenant, 'unit_rent': unit_rent, 'unit_rent_room': unit_rent_room,
        'create_time': now_time, 'use_date': now_time,
        'ele_used': resource_use.this_month_ele - resource_use.last_month_ele,
        'water_used': resource_use.this_month_water - resource_use.last_month_water,
        'gas_used': resource_use.this_month_gas - resource_use.last_month_gas
    }
    ele_money = bill_info.get('ele_used') * charge.unit_ele_money
    water_money = bill_info.get('water_used') * charge.unit_water_money
    gas_money = bill_info.get('gas_used') * charge.unit_gas_money
    bill_info['ele_money'] = ele_money
    bill_info['water_money'] = water_money
    bill_info['gas_money'] = gas_money
    bill_info['rent_money'] = rent_room.rent
    bill_info['total'] = ele_money + water_money + gas_money + rent_room.rent

    bill_info.update(resource_use.dict())

    return insert_bill_info(db, BillInfo(**bill_info))


@bill_app.put("/bill/{unit_rent}/{unit_rent_room}",
              deprecated=True)
async def update_bill(unit_rent: str, unit_rent_room: str, year: int, month: int,
                      db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO check if the unit rental is under this account

    _id = create_bill_info_id(unit_rent, unit_rent_room, year, month)
    update_specify_bill_info(db)


@bill_app.get("/bill/{unit_rent}/{unit_room}/{month}",
              deprecated=True)
async def get_bill_info(unit_rent: str, unit_room: str, month: int,
                        db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO update a new bill
    pass


@bill_app.delete("/bill",
                 deprecated=True)
async def delete_bill(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    # TODO delete a new bill
    pass
