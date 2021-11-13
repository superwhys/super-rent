# coding=gbk
# @File  : curd.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  :
from loguru import logger
from typing import Optional
from pymongo.database import Database
from common.schemas import UnitRent, Tenant, User, UserAuthority


def get_user(db: Database, account_id: str):
    """
    get user: it will find user_name in databases
    :param db:
    :param account_id:
    :return:
    """
    user = db['user'].find_one({'account_id': account_id}, {"_id": 0})
    return user


def get_tenant(db: Database, name: str, id_card: str):
    """
    :param db:
    :param name:
    :param id_card:
    :return:
    """
    tenant = db['tenant'].find_one({'name': name, 'id_card': id_card}, {"_id": 0})
    return tenant


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


def get_unit_rent(db: Database, rent_name: str, account_id: str, authority: str):
    """
    :param authority:
    :param account_id:
    :param db:
    :param rent_name:
    :return:
    """
    user = get_user(db, account_id)
    if user is not None:
        username = user.get('username')
        if authority == UserAuthority.owner:
            rent_id = db['unit_rent'].find_one({'rent_name': rent_name, 'rent_owner': username}, {'_id': 0})
        elif authority == UserAuthority.admin:
            rent_id = db['unit_rent'].find_one({'rent_name': rent_name, 'rent_admin': username}, {'_id': 0})
        else:
            rent_id = None
        return rent_id
    return None


def get_rent_room_by_rent(db: Database, rent_name: str):
    """
    :param rent_name:
    :param db:
    :return:
    """
    rent_room = db['rent_room'].find({'unit_rent': rent_name}, {'_id': 0})
    return list(rent_room)


def get_tenant_info_by_name(db: Database, name: str, unit_rent: str, rent_room: str):
    """
    :param db:
    :param name:
    :param unit_rent:
    :param rent_room:
    :return:
    """

