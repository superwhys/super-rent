# coding=gbk
# @File  : curd.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  :
from loguru import logger
from typing import Optional
from pymongo.database import Database
from common.schemas import UnitRent, Tenant, User


def get_user(db: Database, user_name: str):
    """
    get user: it will find user_name in databases
    :param db:
    :param user_name:
    :return:
    """
    user = db['user'].find_one({'user_name': user_name}, {"_id": 0})
    return user


def create_user(db: Database, user: User):
    """
    create user
    :param db:
    :param user:
    :return:
    """
    try:
        db['user'].insert_one(user.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True


def get_unit_rent_by_name(db: Database, rent_owner: Optional[str] = None, rent_admin: Optional[str] = None):
    """
    get unit_rent by name
    :param db:
    :param rent_owner:
    :param rent_admin:
    :return:
    """
    if rent_owner is None and rent_admin is None:
        unit_rent_lst = db['unit_rent'].find({}, {'_id': 0})
    elif rent_owner and rent_admin:
        unit_rent_lst = db['unit_rent'].find({'rent_owner': rent_owner, 'rent_admin': rent_admin}, {'_id': 0})
    elif rent_owner:
        unit_rent_lst = db['unit_rent'].find({'rent_owner': rent_owner}, {'_id': 0})
    else:
        unit_rent_lst = db['unit_rent'].find({'rent_admin': rent_admin}, {'_id': 0})
    return list(unit_rent_lst)


def get_unit_rent(db: Database, rent_name: Optional[str] = None):
    """
    get user: rent_name is a Optional parameter, if None, it will find all
    :param db:
    :param rent_name:
    :return: 
    """
    return db['unit_rent'].find({'rent_name': rent_name}, {"_id": 0})


def get_unit_rent_room(db: Database, unit_rent_name: str):
    """
    get the room in the given unit rent
    :param db:
    :param unit_rent_name:
    :return:
    """
    unit_rent_id = db['unit_rent'].find({'rent_name': unit_rent_name}, {'rentId': 1, "_id": 0})
    rent_room_lst = db['rent_room'].find({'unit_rent_id': unit_rent_id}, {"_id": 0})
    return rent_room_lst


def create_unit_rent(db: Database, unit_rent: UnitRent):
    """
    create unit rent and put into database
    :param db:
    :param unit_rent:
    :return:
    """
    try:
        db['unit_rent'].insert_one(unit_rent.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True


def create_tenant(db: Database, tenant: Tenant):
    """
    create tenant and put into database
    :param db:
    :param tenant:
    :return:
    """
    try:
        db['tenant'].insert_one(tenant.dict())
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True
