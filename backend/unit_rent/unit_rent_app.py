# coding=gbk
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main


from loguru import logger
from pymongo.database import Database

from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM, oauth2_schema, credentials_exception

from common.database import get_db
from common.curd import get_unit_rent_by_name, get_unit_rent_id, get_rent_room_by_rent_id
from common.schemas import UnitRentLst, UserAuthority, RentRoomLst, RequestStatus
from common.general_module import get_user_agent, get_user_name_in_token

from fastapi import APIRouter, Depends


unit_rent_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@unit_rent_app.get("/get_unit_rent")
async def get_unit_rent(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    Get the unit rent under the current account authority name
    if account is contractor, it just show the unit rent it has
    if account is owner, it will show all the unit rent it has
    :param db:
    :param token:
    :return:
    """
    # get the username and authority in token
    username, authority = get_user_name_in_token(token)

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


@unit_rent_app.get("/unit_rent_info")
async def get_unit_rent_info(rent_name: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param rent_name:
    :param db:
    :param token:
    :return:
    """
    username, authority = get_user_name_in_token(token)

    unit_rent_id = get_unit_rent_id(db, rent_name, username, authority)
    if unit_rent_id:
        rent_room_lst = get_rent_room_by_rent_id(db, int(unit_rent_id['rentId']))
        logger.info(rent_room_lst[0])
        return RentRoomLst(**{'status': RequestStatus.success,
                              'unit_rent_id': int(unit_rent_id['rentId']),
                              'rent_room_lst': rent_room_lst})
    else:
        return RentRoomLst(**{'status': RequestStatus.error, 'msg': 'rent_name not exits'})
