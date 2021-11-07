#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : createFakeData.py
# @Author: SuperYong
# @Date  : 2021/11/712:12 上午
# @Desc  :

from datetime import datetime, timedelta
from random import choice, randint
from pymongo import MongoClient
from faker import Faker


class FakeData:
    def __init__(self):
        self.fake_count = 1000
        self.fake = Faker(locale='zh_CN')
        self.mongo_con = MongoClient("localhost:27017")
        self.mongo_db = self.mongo_con['super_rent']

        self.unit_rent = [self.fake.address().split(' ')[0] for i in range(100)]
        self.owner_name = [self.fake.name() for i in range(100)]
        self.room_type = ['一房一厅', '二房一厅', '三房一厅', '四房一厅', '单间', '三房两厅']
        self.rent_room_status = ['已出租，本月已缴费', '已出租，本月未缴费', '未出租']
        self.unit_rent_room = {}
        self.tenant = []
        self.unitRent_ownerName_mapping = {}

    def insert_2_mongo(self, table, data):
        # print(data)
        # self.mongo_db[table].insert_one(data)
        pass

    def create_charges(self):
        for i in self.unit_rent:
            data = {
                'unit_rent': i,
                'unit_water_money': randint(3, 10),
                'unit_ele_money': randint(3, 10),
                'unit_gas_money': randint(3, 10),
            }
            self.insert_2_mongo("charges", data)

    def create_unit_rent(self):
        rent_type = ['楼栋', '店铺', '公寓']
        self.unitRent_ownerName_mapping = {
            self.unit_rent[i]: [self.owner_name[i]] for i in range(100)
        }
        for i in range(100):
            unit_rent = {
                'rent_name': self.unit_rent[i],
                'rent_owner': self.unitRent_ownerName_mapping[self.unit_rent[i]][0],
                'rent_admin': self.unitRent_ownerName_mapping[self.unit_rent[i]][0],
                'isContract': False,
                'rent_type': choice(rent_type),
                'rent_address': self.unit_rent[i],
                'start_time': self.fake.date(pattern="%Y-%m-%d %H:%M:%S")
            }
            rent_room_num = randint(5, 60)
            unit_rent['rent_room_num'] = rent_room_num
            self.unitRent_ownerName_mapping[self.unit_rent[i]].append(rent_room_num)
            self.insert_2_mongo('unit_rent', unit_rent)

    def create_rent_room(self):
        for unit_rent in self.unitRent_ownerName_mapping:
            room_num = self.unitRent_ownerName_mapping[unit_rent][1]
            self.unit_rent_room[unit_rent] = [i*100+1 for i in range(1, room_num+1)]
            for i in self.unit_rent_room[unit_rent]:
                data = {
                    'unit_rent_room': i,
                    'unit_rent': unit_rent,
                    'room_type': choice(self.room_type),
                    'rent_time': self.fake.date(pattern="%Y-%m-%d %H:%M:%S"),
                    'rent': randint(1000, 6000),
                    'status': choice(self.rent_room_status),
                    'update_time': datetime.now()
                }
                print(data)
                # self.insert_2_mongo('rent_room', data)

    def create_tenant(self):
        tenant_status = ['无', '租期内', '租期已过']
        self.tenant = [self.fake.name() for i in range(2000)]
        for i in self.tenant:
            unit_rent = choice(self.unit_rent)
            unit_rent_room = self.unit_rent_room[unit_rent].pop(randint(0, len(self.unit_rent_room[unit_rent])-1))
            if len(self.unit_rent_room[unit_rent]) == 0:
                self.unit_rent.remove(unit_rent)
                self.unit_rent_room.pop(unit_rent)
            status = choice(tenant_status)
            data = {
                'name': i,
                'unit_rent': unit_rent,
                'unit_rent_room': unit_rent_room,
                'status': status,
                'phone': self.fake.phone_number(),
                'id_card': self.fake.ssn()
            }
            if status == '无':
                data['rent_plan_time'] = 0
            else:
                data['rent_plan_time'] = randint(1, 12)

            self.insert_2_mongo('tenant', data)

    def create_bill_info(self):
        data = self.mongo_db['tenant'].find()

        for d in data:
            if d['status'] == '无':
                continue
            bill_info = {
                'create_time': datetime.now(),
                'unit_rent': d['unit_rent'],
                'unit_rent_room': d['unit_rent_room'],
                'tenant': d['name'],
                'use_date': datetime.now() + timedelta(days=30),
                'last_month_ele': randint(10, 50),
                'last_month_water': randint(20, 50),
                'last_month_gas': randint(10, 50),
                'this_month_ele': randint(50, 90),
                'this_month_water': randint(50, 100),
                'this_month_gas': randint(50, 90),
            }
            ele_use = bill_info['this_month_ele'] - bill_info['last_month_ele']
            water_use = bill_info['this_month_water'] - bill_info['last_month_water']
            gas_use = bill_info['this_month_gas'] - bill_info['last_month_gas']
            bill_info['ele_used'] = ele_use
            bill_info['water_used'] = water_use
            bill_info['gas_used'] = gas_use

            charge = self.mongo_db['charges'].find_one({'unit_rent': d['unit_rent']})
            bill_info['ele_money'] = charge['unit_ele_money'] * ele_use
            bill_info['water_money'] = charge['unit_water_money'] * water_use
            bill_info['gas_money'] = charge['unit_gas_money'] * gas_use

            bill_info['total'] = bill_info['ele_money'] + bill_info['water_money'] + bill_info['gas_money']
            print(bill_info)
            # self.insert_2_mongo('bill_info', bill_info)
            self.mongo_db['bill_info'].update_one({'unit_rent': bill_info['unit_rent'], 'tenant': bill_info['tenant']}, {'$set': bill_info}, upsert=True)

    def create_index(self):
        self.mongo_db['bill_info'].create_index([('unit_rent', 1)], background=True)
        self.mongo_db['bill_info'].create_index([('unit_rent', 1), ('unit_rent_room', 1)], background=True)
        self.mongo_db['bill_info'].create_index([('unit_rent', 1), ('unit_rent_room', 1), ('use_date', 1)], unique=True, background=True)
        self.mongo_db['charges'].create_index([('unit_rent', 1)], background=True)
        self.mongo_db['rent_room'].create_index([('status', 1)], background=True)
        self.mongo_db['rent_room'].create_index([('tenant', 1)], background=True)
        self.mongo_db['rent_room'].create_index([('unit_rent', 1), ('unit_rent_room', 1)], background=True, unique=True)
        self.mongo_db['tenant'].create_index([('name', 1)], background=True)
        self.mongo_db['tenant'].create_index([('name', 1), ('id_card', 1)], background=True, unique=True)
        self.mongo_db['tenant'].create_index([('status', 1)], background=True)
        self.mongo_db['tenant'].create_index([('status', 1), ('unit_rent', 1)], background=True)
        self.mongo_db['unit_rent'].create_index([('rent_name', 1)], background=True)
        self.mongo_db['unit_rent'].create_index([('rent_type', 1)], background=True)
        self.mongo_db['user'].create_index([('authority', 1)], background=True)
        self.mongo_db['user'].create_index([('user_name', 1)], background=True)

    def update_rent_room_tenant(self):
        data = self.mongo_db['tenant'].find()
        for d in data:
            self.mongo_db['rent_room'].update_one({'unit_rent': d['unit_rent'], 'unit_rent_room': d['unit_rent_room']}, {'$set': {'tenant': d['name']}}, upsert=True)

    def run(self):
        # self.create_charges()
        # self.create_unit_rent()
        # self.create_rent_room()
        # self.create_tenant()
        # self.create_bill_info()
        self.update_rent_room_tenant()
        # self.create_index()


if __name__ == '__main__':
    fd = FakeData()
    fd.run()
