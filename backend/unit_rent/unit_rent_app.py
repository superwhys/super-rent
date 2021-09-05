# coding=gbk
# @File  : user_app.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main


from loguru import logger
from pymongo.database import Database

from jose import JWTError, jwt
from config import SECRET_KEY, ALGORITHM, oauth2_schema

from common.database import get_db
from common.curd import get_unit_rent_by_name
from common.schemas import UnitRentLst, UserAuthority
from common.general_module import get_user_agent

from fastapi import APIRouter, Depends, HTTPException, status


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
    credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    # get the username and authority in token
    try:
        token_decode = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])
        username = token_decode.get("sub")
        if username is None:
            raise credentials_exception

        authority = token_decode.get('auth')
    except JWTError:
        raise credentials_exception

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

