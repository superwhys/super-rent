#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : curd.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  :

from typing import Optional
from schemas import UnitRent, Tenant


def get_user(db, user_name: Optional[str] = None):
    """
    get user: user_name is a Optional parameter, if None, it will find all
    :param db:
    :param user_name:
    :return:
    """
    pass


def get_unit_rent(db, rent_name: Optional[str] = None):
    """
    get user: rent_name is a Optional parameter, if None, it will find all
    :param db:
    :param rent_name:
    :return: 
    """
    pass


def create_unit_rent(db, unit_rent: UnitRent):
    """
    create unit rent and put into database
    :param db:
    :param unit_rent:
    :return:
    """
    pass


def create_tenant(db, tenant: Tenant):
    """
    create tenant and put into database
    :param db:
    :param tenant:
    :return:
    """
    pass





