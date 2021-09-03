#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : curd.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  :
from loguru import logger
from typing import Optional
from schemas import UnitRent, Tenant, User


def get_user(db, user_name: str) -> dict:
    """
    get user: it will find user_name in databases
    :param db:
    :param user_name:
    :return:
    """
    user = db['user'].find_one({'user_name': user_name}, {"_id": 0})
    return user


async def create_user(db, user: User):
    """
    create user
    :param db:
    :param user:
    :return:
    """
    try:
        await db['user'].insert_one(user.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True


async def get_unit_rent(db, rent_name: Optional[str] = None):
    """
    get user: rent_name is a Optional parameter, if None, it will find all
    :param db:
    :param rent_name:
    :return: 
    """
    return await db['unit_rent'].find({'rent_name': rent_name}, {"_id": 0})


async def get_unit_rent_room(db, unit_rent_name: str):
    """
    get the room in the given unit rent
    :param db:
    :param unit_rent_name:
    :return:
    """
    unit_rent_id = await db['unit_rent'].find({'rent_name': unit_rent_name}, {'rentId': 1, "_id": 0})
    rent_room_lst = await db['rent_room'].find({'unit_rent_id': unit_rent_id}, {"_id": 0})
    return rent_room_lst


async def create_unit_rent(db, unit_rent: UnitRent):
    """
    create unit rent and put into database
    :param db:
    :param unit_rent:
    :return:
    """
    try:
        await db['unit_rent'].insert_one(unit_rent.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True


async def create_tenant(db, tenant: Tenant):
    """
    create tenant and put into database
    :param db:
    :param tenant:
    :return:
    """
    try:
        await db['tenant'].insert_one(tenant.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True





