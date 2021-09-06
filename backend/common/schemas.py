# coding=gbk
# @File  : schemas.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : Field constraint

from enum import Enum
from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class RequestStatus(str, Enum):
    success = "success"
    error = "error"


class RentBase(BaseModel):
    status: RequestStatus
    msg: Optional[str]


class UserAuthority(str, Enum):
    admin = "admin"
    owner = "owner"
    contractor = "contractor"


class RentType(str, Enum):
    apartment = "公寓"
    shop = "店铺"
    building = "楼栋"


class TenantStatus(str, Enum):
    no_rent = '无'
    in_rent = '租期内'
    out_rent = '租期已过'


class RentStatus(str, Enum):
    #  已出租，本月已缴费
    rent_and_paid = "已出租，本月已缴费"
    # 已出租， 本月未缴费
    rent_and_noPay = "已出租，本月未缴费"
    # 未出租
    no_rent = "未出租"


class Token(BaseModel):
    access_token: str
    token_type: str


class RegisterStatus(BaseModel):
    status: bool
    msg: Optional[str] = None
    token: Optional[Token] = None


##################################
##################################
##################################


class Charge(BaseModel):
    unit_rent: str
    unit_water_money: int
    unit_ele_money: int
    unit_gas_money: int


class User(BaseModel):
    user_name: str
    password: str
    authority: UserAuthority
    phone: str


class UnitRent(BaseModel):
    rent_name: str
    rent_owner: str
    rent_admin: str
    isContract: bool
    rent_type: RentType
    rent_address: str
    start_time: datetime
    rent_room_num: int


class UnitRentLst(BaseModel):
    rent_owner: Optional[str] = None
    rent_admin: Optional[str] = None
    unit_rent_lst: List[UnitRent]


class RentRoom(BaseModel):
    unit_rent: str
    unit_rent_room: str
    room_type: str
    rent_time: datetime
    rent: int
    status: RentStatus


class Tenant(BaseModel):
    name: str
    unit_rent: Optional[str] = None
    unit_rent_root: Optional[str] = None
    status: Optional[TenantStatus] = TenantStatus.no_rent
    rent_plan_time: Optional[int] = 0
    phone: str
    id_card: str


class BillInfo(BaseModel):
    tenant: str
    unit_rent: str
    unit_rent_room: str
    create_time: datetime
    use_date: str
    last_month_water: int
    last_month_ele: int
    last_month_gas: int
    this_month_water: int
    this_month_ele: int
    this_month_gas: int
    ele_used: int
    water_used: int
    gas_used: int
    ele_money: int
    water_money: int
    gas_money: int
    total: int


class RentRoomLst(RentBase):
    unit_rent_id: Optional[int]
    rent_room_lst: Optional[List[RentRoom]] = None
