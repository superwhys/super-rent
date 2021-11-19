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
    none = "None"


class UserAuthority(str, Enum):
    admin = "admin"
    owner = "owner"
    contractor = "contractor"


class RentType(str, Enum):
    none = None
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


class StatusBase(BaseModel):
    status: RequestStatus = RequestStatus.none
    msg: Optional[str] = None


class BaseToken(BaseModel):
    access_token: str
    token_type: str


class RegisterStatus(StatusBase):
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


class UnitRent(BaseModel):
    rent_name: str
    rent_owner: str
    rent_admin: str
    isContract: bool
    rent_type: RentType
    rent_address: str
    start_time: datetime
    rent_room_num: int


class Tenant(BaseModel):
    name: str
    unit_rent: Optional[str] = None
    unit_rent_room: Optional[str] = None
    status: Optional[TenantStatus] = TenantStatus.no_rent
    rent_plan_time: Optional[int] = 0
    phone: str
    id_card: str


class RentRoom(BaseModel):
    unit_rent: str
    unit_rent_room: str
    room_type: str
    rent_time: datetime = datetime(1999, 9, 15, 9, 15, 15)
    rent: int
    status: RentStatus = RentStatus.no_rent
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


#########################################
#########################################
#########################################
# Response Model


class LoginRes(StatusBase):
    username: Optional[str] = None
    access_token: Optional[str] = None
    token_type: Optional[str] = None


class TenantInfoRes(StatusBase):
    tenant: Optional[Tenant] = None


class HomeUnitRentInfo(BaseModel):
    rent_name: str
    rent_address: str
    rent_owner: str
    rent_type: RentType = RentType.none
    start_time: datetime
    rent_room_num: int
    this_month_price: int


class RentTypeNum(BaseModel):
    rent_type_name: str
    rent_num: int


class UserRentInfo(StatusBase):
    """
    get user info response model
    """
    account_id: str
    username: str
    totalPrice: int
    each_rental_info: List[HomeUnitRentInfo]
    rent_type_num: List[RentTypeNum]


class UnitRentLst(StatusBase):
    """
    get_all_unit_rental response model
    """
    rental_owner: Optional[str] = None
    rental_admin: Optional[str] = None
    unit_rental_lst: List[UnitRent]


class RentRoomLst(StatusBase):
    """
    get_all_unit_rental_room response model
    """
    unit_rental: Optional[str]
    rental_room_lst: Optional[List[RentRoom]] = None


class SpecifyUnitRental(StatusBase):
    """
    get_specify_unit_rental response model
    """
    unit_rental: Optional[UnitRent] = None
