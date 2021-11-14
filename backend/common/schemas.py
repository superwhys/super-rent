# coding=gbk
# @File  : schemas.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 ����
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
    msg: Optional[str] = None


class UserAuthority(str, Enum):
    admin = "admin"
    owner = "owner"
    contractor = "contractor"


class RentType(str, Enum):
    apartment = "��Ԣ"
    shop = "����"
    building = "¥��"


class TenantStatus(str, Enum):
    no_rent = '��'
    in_rent = '������'
    out_rent = '�����ѹ�'


class RentStatus(str, Enum):
    #  �ѳ��⣬�����ѽɷ�
    rent_and_paid = "�ѳ��⣬�����ѽɷ�"
    # �ѳ��⣬ ����δ�ɷ�
    rent_and_noPay = "�ѳ��⣬����δ�ɷ�"
    # δ����
    no_rent = "δ����"


class BaseToken(BaseModel):
    access_token: str
    token_type: str


class TokenStatus(BaseToken):
    status: RequestStatus
    msg: Optional[str] = None


class RegisterStatus(BaseModel):
    status: RequestStatus
    msg: Optional[str] = None
    token: Optional[BaseToken] = None


##################################
##################################
##################################


class Charge(BaseModel):
    unit_rent: str
    unit_water_money: int
    unit_ele_money: int
    unit_gas_money: int


class User(BaseModel):
    account_id: str
    user_name: str
    password: str
    authority: UserAuthority
    phone: Optional[str] = "00000000000"


class Tenant(BaseModel):
    name: str
    unit_rent: Optional[str] = None
    unit_rent_room: Optional[str] = None
    status: Optional[TenantStatus] = TenantStatus.no_rent
    rent_plan_time: Optional[int] = 0
    phone: str
    id_card: str


class UnitRent(BaseModel):
    rent_name: str
    rent_owner: str
    rent_admin: str
    isContract: bool
    rent_type: RentType
    rent_address: str
    start_time: datetime
    rent_room_num: int


class UnitRentLst(RentBase):
    rental_owner: Optional[str] = None
    rental_admin: Optional[str] = None
    unit_rental_lst: List[UnitRent]


class RentRoom(BaseModel):
    unit_rent: str
    unit_rent_room: str
    room_type: str
    rent_time: datetime
    rent: int
    status: RentStatus
    tenant: Optional[str] = None


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
    unit_rental: Optional[str]
    rental_room_lst: Optional[List[RentRoom]] = None
