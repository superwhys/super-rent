# coding=gbk
# @File  : add_data_to_mongo.py
# @Author: SuperYong
# @Date  : 2021/9/211:23 下午
# @Desc  :
import json
from json import loads
import pymongo
import re


def add_data_to_mongo(paths: list):
    table_name_re = r"\.\/(.*?)\.json"

    client = pymongo.MongoClient('mongodb://127.0.0.1:27017')
    # client = pymongo.MongoClient('mongodb://superyong.top:27018')
    # client = pymongo.MongoClient(host="mongo", port=27017)
    db = client['super_rent']

    for path in paths:
        with open(path, 'r', encoding='utf-8') as f:
            data = loads(f.read())
            print(data)
            for d in data:
                table_name = re.findall(table_name_re, path)[0]
                table = db[table_name]
                table.insert_one(d)

    client.close()


if __name__ == '__main__':
    bill_info_path = './bill_info.json'
    charges_path = './charges.json'
    tenant_path = './tenant.json'
    unit_rent_path = './unit_rent.json'
    rent_room_path = './rent_room.json'
    user_path = './user.json'

    # path_lst = [bill_info_path, charges_path, tenant_path,
    #             unit_rent_path, rent_room_path, user_path]

    path_lst = [rent_room_path]

    add_data_to_mongo(path_lst)
