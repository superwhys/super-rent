# coding=gbk
# @File  : database.py
# @Author: SuperYong
# @Date  : 2021/9/19:54 下午
# @Desc  : database setting

from pymongo import MongoClient


def get_client(host, port):
    return MongoClient(host, port)


def get_table(db, table_name):
    """
    get mongodb table
    :param db:
    :param table_name:
    :return:
    """
    return db[table_name]
