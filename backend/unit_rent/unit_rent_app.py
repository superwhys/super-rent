# coding=gbk
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main


from loguru import logger
from pymongo.database import Database


from config import oauth2_schema
from descriptions import get_unit_rent_desc, get_unit_rent_info_desc

from common.database import get_db
from common.curd import get_unit_rent_by_name, get_unit_rent, get_rent_room_by_rent, get_user
from common.schemas import UnitRentLst, UserAuthority, RentRoomLst, RequestStatus
from common.general_module import get_user_agent, get_account_in_token

from fastapi import APIRouter, Depends


unit_rent_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@unit_rent_app.get("/unit-rent",
                   summary='获取某账号名下所有出租单位',
                   description=get_unit_rent_desc)
async def get_all_unit_rent(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    Get the unit rent under the current account authority name
    if account is contractor, it just show the unit rent it has
    if account is owner, it will show all the unit rent it has
    :param db:
    :param token:
    :return:
    """
    # get the username and authority in token
    account_id, authority = get_account_in_token(token)
    user = get_user(db, account_id)
    if user:
        username = user.get('username')
        # get different information according to different authority
        unit_rent = []
        if authority == UserAuthority.admin:
            unit_rent = get_unit_rent_by_name(db)
        if authority == UserAuthority.owner:
            unit_rent = get_unit_rent_by_name(db, rent_owner=username)
        if authority == UserAuthority.contractor:
            unit_rent = get_unit_rent_by_name(db, rent_admin=username)
        unit_rent_lst = {'rent_owner': username, 'unit_rent_lst': unit_rent}
        logger.info(f'get_unit_rent_by_name: {username}, {unit_rent_lst}')
        return UnitRentLst(**unit_rent_lst)
    return UnitRentLst(**{'status': RequestStatus.error, 'msg': 'owner not exits'})


@unit_rent_app.get("/unit_rent_info",
                   summary='获取某出租单位下所有出租单元',
                   description=get_unit_rent_info_desc)
async def get_unit_rent_info(rent_name: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param rent_name:
    :param db:
    :param token:
    :return:
    """
    account_id, authority = get_account_in_token(token)

    unit_rent = get_unit_rent(db, rent_name, account_id, authority)
    if unit_rent:
        rent_room_lst = get_rent_room_by_rent(db, unit_rent['rent_name'])
        return RentRoomLst(**{'status': RequestStatus.success,
                              'unit_rent': unit_rent['rent_name'],
                              'rent_room_lst': rent_room_lst})
    else:
        return RentRoomLst(**{'status': RequestStatus.error, 'msg': 'rent_name or owner not exits'})
