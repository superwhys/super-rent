# coding=gbk
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main

from loguru import logger
from pymongo.database import Database

from config import oauth2_schema, ERROR_HEADER, credentials_exception
from descriptions import get_all_unit_rental_desc, get_unit_rental_desc, get_all_unit_rental_room_desc, get_unit_rental_room_desc

from common.database import get_db
from common.curd import get_unit_rent_by_name, get_unit_rent, get_rent_room_by_rent, get_user, get_specify_rent_room
from common.schemas import UnitRentLst, UserAuthority, RentRoomLst, RequestStatus, RentRoom, SpecifyUnitRental
from common.general_module import get_user_agent, get_account_in_token

from fastapi import APIRouter, Depends, HTTPException, status

unit_rent_app = APIRouter(
    dependencies=[Depends(get_user_agent)]
)


@unit_rent_app.get("/unit-rental",
                   summary='获取当前账号名下所有出租单位',
                   description=get_all_unit_rental_desc)
async def get_all_unit_rental(db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    Get the unit rental under the current account authority name
    if account is contractor, it just show the unit rent it has
    if account is owner, it will show all the unit rent it has
    :param token:
    :param db:
    :return:
    """
    # get the username and authority in token
    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception

    user = get_user(db, account_id)
    if user:
        username = user.get('user_name')
        # get different information according to different authority
        unit_rent = []
        if authority == UserAuthority.admin:
            unit_rent = get_unit_rent_by_name(db)
        if authority == UserAuthority.owner:
            unit_rent = get_unit_rent_by_name(db, rent_owner=username)
        if authority == UserAuthority.contractor:
            unit_rent = get_unit_rent_by_name(db, rent_admin=username)
        unit_rent_lst = {'rental_owner': username, 'unit_rental_lst': unit_rent, 'status': RequestStatus.success}
        # logger.info(f'get_unit_rental_by_name: {username}, {unit_rent_lst}')
        return UnitRentLst(**unit_rent_lst)
    return UnitRentLst(**{'status': RequestStatus.error, 'msg': 'owner not exits'})


@unit_rent_app.get("/unit-rental/{rental_name}",
                   summary='获取当前账号名下指定出租单位',
                   description=get_unit_rental_desc)
async def get_specify_unit_rental(rental_name: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    Get the unit rental for specified
    :param rental_name:
    :param token:
    :param db:
    :return:
    """
    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception

    if authority not in {UserAuthority.admin, UserAuthority.owner, UserAuthority.contractor}:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={'status': RequestStatus.error, 'msg': "Permissions error"},
            headers=ERROR_HEADER
        )
    unit_rental = get_unit_rent(db, rental_name, account_id, authority)
    res = {'status': RequestStatus.success, 'unit_rental': unit_rental}
    if unit_rental:
        return SpecifyUnitRental(**res)
    return SpecifyUnitRental(**{'status': RequestStatus.error, 'msg': 'unit rent not found'})


@unit_rent_app.get("/unit_rental_room/{rental_name}",
                   summary='获取当前账号名下某出租单位下所有出租单元',
                   description=get_all_unit_rental_room_desc)
async def get_all_unit_rental_room(rental_name: str, db: Database = Depends(get_db), token: str = Depends(oauth2_schema)):
    """
    :param rental_name:
    :param token:
    :param db:
    :return:
    """
    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception

    # Check whether the unit rental exists
    unit_rental = get_unit_rent(db, rental_name, account_id, authority)
    if unit_rental:
        rental_room_lst = get_rent_room_by_rent(db, unit_rental['rent_name'])
        logger.debug(rental_room_lst)
        return RentRoomLst(**{'status': RequestStatus.success,
                              'unit_rental': unit_rental['rent_name'],
                              'rental_room_lst': rental_room_lst})
    else:
        return RentRoomLst(**{'status': RequestStatus.error, 'msg': 'rent_name or owner not exits'})


@unit_rent_app.get("/unit_rental_room/{rental_name}/query/{room_id}",
                   summary='获取当前账号名下某出租单位下指定出租单元',
                   response_model=RentRoom,
                   description=get_unit_rental_room_desc)
async def get_unit_rental_room(rental_name: str, room_id: int,
                               db: Database = Depends(get_db),
                               token: str = Depends(oauth2_schema)):
    """
    :param rental_name:
    :param room_id:
    :param token:
    :param db:
    :return:
    """
    account_id, authority = get_account_in_token(token)
    if account_id is None or authority is None:
        raise credentials_exception
    user = get_user(db, account_id)

    if authority == UserAuthority.admin:
        unit_rent_lst = get_unit_rent_by_name(db)
    elif authority == UserAuthority.owner:
        unit_rent_lst = get_unit_rent_by_name(db, rent_owner=user['user_name'])
    else:
        unit_rent_lst = get_unit_rent_by_name(db, rent_admin=user['user_name'])

    unit_rent_name_lst = set([unit_rent['rent_name'] for unit_rent in unit_rent_lst])

    if rental_name not in unit_rent_name_lst:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail={'status': RequestStatus.error, 'msg': "this account don't has this unit rent"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    rent_room = get_specify_rent_room(db, rental_name, room_id)
    if rent_room is None:
        raise HTTPException(
            status.HTTP_404_NOT_FOUND,
            detail={'status': RequestStatus.error, 'msg': "this account don't has this unit rent"},
            headers={"WWW-Authenticate": "Bearer"},
        )
    return RentRoom(**rent_room)
