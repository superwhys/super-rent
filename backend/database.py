#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : database.py
# @Author: SuperYong
# @Date  : 2021/9/19:54 下午
# @Desc  : database setting

from pymongo import MongoClient


def get_client(ip):
    return MongoClient(ip)


def get_table(db, table_name):
    """
    get mongodb table
    :param db:
    :param table_name:
    :return:
    """
    return db[table_name]
