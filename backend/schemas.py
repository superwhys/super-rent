#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : schemas.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : Field constraint

from enum import Enum
from datetime import datetime
from pydantic import BaseModel


class RentType(str, Enum):
    apartment = "公寓"
    shop = "店铺"
    building = "楼栋"


class UnitRent(BaseModel):
    rentId: int
    rent_name: str
    rent_owner: str
    rent_admin: str
    isContract: bool
    rent_type: RentType
    rent_address: str
    start_time: datetime
    rent_room_num: int


class Tenant(BaseModel):
    tenantId: int
    name: str
    unit_rent_id: int
    unit_rent_root_id: int
    phone: str
    id_card: str
