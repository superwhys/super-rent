#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : database.py
# @Author: SuperYong
# @Date  : 2021/9/19:54 下午
# @Desc  : database setting

from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['super_rent']


def get_table(db_name, table_name):
    """
    get mongodb table
    :param db_name:
    :param table_name:
    :return:
    """
    return db_name[table_name]
