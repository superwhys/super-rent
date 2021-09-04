#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : test.py
# @Author: SuperYong
# @Date  : 2021/9/47:20 下午
# @Desc  :

import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJcdTY3NjhcdTZkNjlcdTY1ODciLCJhdXRoIjoib3duZXIiLCJjcmVhdGVfdGltZSI6IjIwMjEtMDktMDQgMjA6MTE6MTciLCJleHAiOjE2MzA3NTkyNzd9.jl-uX6EsW55Yp1bNoA_AEDx7dpQ_bffctfGdcRsKzUA'
}

res = requests.get('http://localhost:8000/rent/get_unit_rent', headers=headers)
print(res.text)
