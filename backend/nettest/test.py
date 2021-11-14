# coding=gbk
# @File  : test.py
# @Author: SuperYong
# @Date  : 2021/9/47:20 下午
# @Desc  :

import requests

headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0b3duZXIiLCJhdXRoIjoib3duZXIiLCJjcmVhdGVfdGltZSI6IjIwMjEtMTEtMTQgMjA6MjI6MDkiLCJleHAiOjE2MzY4OTQzMjl9.25I3ThBOuDlsMmSZCjkF7MRxR1_cFfH5zuhZRU2i-_s',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}

params = (
    ('account_id', 'testowner'),
)

response = requests.get('http://localhost:8000/rent/v1/user', headers=headers, params=params)
print(response.text)