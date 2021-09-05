# coding=gbk
# @File  : database.py
# @Author: SuperYong
# @Date  : 2021/9/19:54 下午
# @Desc  : database setting

from loguru import logger
from pymongo import MongoClient
from config import HOST, PORT


def get_client(host, port):
    return MongoClient(host, port)


def get_db():
    client = get_client(host=HOST, port=PORT)
    try:
        logger.info('get client')
        yield client['super_rent']
    finally:
        client.close()
        logger.info('client close')


def get_table(db, table_name):
    """
    get mongodb table
    :param db:
    :param table_name:
    :return:
    """
    return db[table_name]
