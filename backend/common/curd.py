# coding=gbk
# @File  : curd.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 ????
# @Desc  :
from hashlib import md5
from loguru import logger
from typing import Optional
from collections import Counter
from pymongo.database import Database
from fastapi import HTTPException, status
from common.schemas import UnitRent, Tenant, User, UserAuthority, UpdateInfo, UpdateUser, RequestStatus, Charge, \
    BillInfo, RentRoom


def get_auth_code(db: Database, auth_code) -> bool:
    """
    Determine whether the authorization code is useful
    :param auth_code:
    :param db:
    :return:
    """
    ac = db['auth_code'].find_one({'auth_code': auth_code})
    if ac is None:
        return False
    return True


def get_user(db: Database, account_id: str) -> dict:
    """
    get user: it will find user_name in databases
    :param db:
    :param account_id:
    :return:
    """
    user = db['user'].find_one({'account_id': account_id}, {"_id": 0})
    return user


def get_tenant(db: Database, name: str, id_card: str) -> dict:
    """
    :param db:
    :param name:
    :param id_card:
    :return:
    """
    tenant = db['tenant'].find_one({'name': name, 'id_card': id_card}, {"_id": 0})
    return tenant


def create_user(db: Database, user: User) -> bool:
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


def create_unit_rent(db: Database, unit_rent: UnitRent) -> bool:
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


def create_tenant(db: Database, tenant: Tenant) -> bool:
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


def get_unit_rent_by_name(db: Database, rent_owner: Optional[str] = None, rent_admin: Optional[str] = None) -> list:
    """
    get all the unit rental under the user
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


def get_unit_rent_room(db: Database, unit_rent_name: str) -> list:
    """
    get the room in the given unit rent
    :param db:
    :param unit_rent_name:
    :return:
    """
    unit_rent_id = db['unit_rent'].find({'rent_name': unit_rent_name}, {'rentId': 1, "_id": 0})
    rent_room_lst = db['rent_room'].find({'unit_rent_id': unit_rent_id}, {"_id": 0})
    return rent_room_lst


def get_specify_rent_room(db: Database, rent_name: str, room_id: int) -> dict or None:
    data = db['rent_room'].find_one({'unit_rent': rent_name, 'unit_rent_room': room_id}, {'_id': 0})
    logger.debug(data)
    return data


def get_unit_rent(db: Database, rent_name: str, account_id: str, authority: str) -> dict or None:
    """
    get the specify unit rental information
    :param authority:
    :param account_id:
    :param rent_name:
    :param db:
    :return:
    """
    user = get_user(db, account_id)
    if user is not None:

        username = user.get('user_name')
        if authority == UserAuthority.owner:
            rent_id = db['unit_rent'].find_one({'rent_name': rent_name, 'rent_owner': username}, {'_id': 0})
        elif authority == UserAuthority.contractor:
            rent_id = db['unit_rent'].find_one({'rent_name': rent_name, 'rent_admin': username}, {'_id': 0})
        elif authority == UserAuthority.admin:
            rent_id = db['unit_rent'].find_one({'rent_name': rent_name}, {'_id': 0})
        else:
            rent_id = None
        logger.debug(rent_id)
        return rent_id
    return None


def get_rent_room_by_rent(db: Database, rent_name: str) -> list:
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
    pass


def get_user_rent_info_data(db: Database, account_id: str, authority: UserAuthority) -> dict:
    """
    get the user rental info in database
    include each rent_type num,
    and the price of all unit rental
    :param authority:
    :param account_id:
    :param db:
    :return: a dict
    """
    try:
        if authority == UserAuthority.admin:
            unit_rent_lst = get_unit_rent_by_name(db)
            # rent type number
            rent_type_num = db['unit_rent'].aggregate([{'$group': {'_id': '$rent_type', 'rent_num': {'$sum': 1}}},
                                                       {'$project': {'_id': 0, 'rent_type_name': '$_id',
                                                                     'rent_num': 1}}])
            rent_type_num = list(rent_type_num)
            # each unit rental price
            unit_rental_price = db['bill_info'].aggregate([{'$group': {'_id': '$unit_rent',
                                                                       'total_price': {'$sum': '$total'}}},
                                                           {'$project': {'_id': 0, 'unit_rent': '$_id',
                                                                         'total_price': 1}}])
            unit_rental_price_fin = {price_dic['unit_rent']: price_dic['total_price'] for price_dic in
                                     unit_rental_price}
            # total rental price
            total_price = db['bill_info'].aggregate([{'$group': {'_id': "null", 'total_price': {'$sum': '$total'}}},
                                                     {'$project': {'_id': 0}}])
            total_price = list(total_price)[0]
        else:
            # get the info in specify user
            user = get_user(db, account_id)
            if authority == UserAuthority.owner:
                unit_rent_lst = get_unit_rent_by_name(db, rent_owner=user.get('user_name'))
            else:
                unit_rent_lst = get_unit_rent_by_name(db, rent_admin=user.get('user_name'))

            rent_type_lst = [unit_rental['rent_type'] for unit_rental in unit_rent_lst]
            rent_name_lst = [unit_rental['rent_name'] for unit_rental in unit_rent_lst]
            rent_type_counter = Counter(rent_type_lst)
            # rent type number
            rent_type_num = [{'rent_type_name': count_key, 'rent_num': rent_type_counter[count_key]}
                             for count_key in rent_type_counter]
            # each unit rental price
            unit_rental_price = db['bill_info'].aggregate([{'$match': {'unit_rent': {'$in': rent_name_lst}}},
                                                           {'$group': {'_id': '$unit_rent',
                                                                       'total_price': {'$sum': '$total'}}},
                                                           {'$project': {'_id': 0, 'unit_rent': '$_id',
                                                                         'total_price': 1}}])
            unit_rental_price_fin = {price_dic['unit_rent']: price_dic['total_price'] for price_dic in
                                     unit_rental_price}
            # total rental price
            total_price = db['bill_info'].aggregate([{'$match': {'unit_rent': {'$in': rent_name_lst}}},
                                                     {'$group': {'_id': "null", 'total_price': {'$sum': '$total'}}},
                                                     {'$project': {'_id': 0}}])
            total_price = list(total_price)[0]

        unit_rental_lst = []
        for unit_rent in unit_rent_lst:
            unit_rental = {'rent_name': unit_rent['rent_name'],
                           'rent_address': unit_rent['rent_address'],
                           'rent_owner': unit_rent['rent_owner'],
                           'rent_type': unit_rent['rent_type'],
                           'start_time': unit_rent['start_time'],
                           'rent_room_num': unit_rent['rent_room_num'],
                           'this_month_price': unit_rental_price_fin.get(unit_rent['rent_name'])}
            unit_rental_lst.append(unit_rental)
        logger.debug(unit_rental_lst)
        return {'totalPrice': total_price['total_price'],
                'rent_type_num': rent_type_num,
                'each_rental_info': unit_rental_lst}
    except Exception as e:
        logger.debug(e)
        raise HTTPException(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'status': RequestStatus.error, 'msg': "get user info function error"},
            headers={"WWW-Authenticate": "Bearer"},
        )


def update_user_info_db(db: Database, account_id: str, update_info: UpdateUser):
    update_dic = {info.type.value: info.msg for info in update_info.update_info}
    logger.debug(update_dic)
    try:
        db['user'].update_one({'account_id': account_id}, {'$set': update_dic}, upsert=True)
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE,
            detail={'status': RequestStatus.error, 'msg': "server not acceptable"},
            headers={"WWW-Authenticate": "Bearer"},
        )
    else:
        return {'status': RequestStatus.success}


def get_charges_data(db: Database, unit_rent: str):
    """
    get specify unit_rent charge
    :param db:
    :param unit_rent:
    :return:
    """
    charge = db['charges'].find_one({'unit_rent': unit_rent}, {'_id': 0})
    return Charge(**charge)


def get_rent_room(db: Database, unit_rent: str, unit_rent_room: str):
    """
    get_rent_room info
    :param db:
    :param unit_rent:
    :param unit_rent_room:
    :return:
    """
    data = db['rent_room'].find_one({'unit_rent': unit_rent, 'unit_rent_room': unit_rent_room}, {'_id': 0})
    return RentRoom(**data)


def create_bill_info_id(unit_rent: str, unit_rent_room: str, year: int, month: int):
    return md5(f'{unit_rent}-{unit_rent_room}-{year}-{month}'.encode('utf-8')).hexdigest()


def insert_bill_info(db: Database, bill_info: BillInfo):
    """
    create bill_info _id and insert into db
    :param db:
    :param bill_info:
    :return:
    """
    # md5(unit_rent - unit_rent_room - year - month)
    try:
        data = bill_info.dict()
        now_time = data.get('create_time')
        unit_rent = data.get('unit_rent')
        unit_rent_room = data.get("unit_rent_room")
        _id = create_bill_info_id(unit_rent, unit_rent_room, now_time.year, now_time.month)
        data['_id'] = _id
        db['bill_info'].insert_one(data)
        return {'status': RequestStatus.success}
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'status': RequestStatus.error, 'msg': 'server not acceptable'}
        )


def update_specify_bill_info(db: Database, _id: str, update_data: dict):
    try:
        db['bill_info'].update_one({'_id': _id}, {'$set': update_data})
    except Exception as e:
        logger.error(e)
        return False
    else:
        return True


def get_specify_bill_info(db: Database, _id: str):
    data = db['bill_info'].find_one({'_id': _id})
    return data
