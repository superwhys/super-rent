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


class User(BaseModel):
    user_name: str
    password: str
    authority: UserAuthority
    phone: str


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


class UnitRentLst(BaseModel):
    rent_owner: Optional[str] = None
    rent_admin: Optional[str] = None
    unit_rent_lst: List[UnitRent]


class RentRoom(BaseModel):
    unit_rent_room_id: int
    unit_rent_id: int
    tenant_id: int
    room: str
    room_type: str
    rent_time: datetime
    rent_plan_time: int
    rent: int
    status: RentStatus
    use_info_id: int


class Tenant(BaseModel):
    tenantId: int
    name: str
    unit_rent_id: int
    unit_rent_root_id: int
    phone: str
    id_card: str


class RentRoomLst(RentBase):
    unit_rent_id: Optional[int]
    rent_room_lst: Optional[List[RentRoom]] = None
