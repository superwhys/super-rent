# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : get_encrypt_pwd.py
# @Author  : SuperYong
# @Date    : 2021/11/14 11:25 上午
# @Desc    :

from time import time
from hashlib import md5
from base64 import b64encode


def get_encrypt_pwd(pwd: str):
    now = str(int(time()))

    pwd_encode_utf8 = pwd.encode('utf-8')
    pwd_md5 = md5(pwd_encode_utf8).hexdigest()
    pwd_plain_text = f'{now[:5]}-{pwd_md5}-{now[5:]}'
    b64encode_pwd = b64encode(pwd_plain_text.encode('utf-8'))
    return b64encode_pwd.decode('utf-8')


def get_auth_code():
    auth_code = "SuperRent-Auth-Code"
    name = "SuperYong"
    now = str(int(time()))

    auth_code_md5 = md5(auth_code.encode("utf-8")).hexdigest()
    name_md5 = md5(name.encode("utf-8")).hexdigest()

    text = f'{now[:5]}-{name_md5}-{auth_code_md5}-{now[5:]}'
    print(text)
    text_b64 = b64encode(text.encode("utf-8")).decode("utf-8")

    print(text_b64)


if __name__ == '__main__':
    encrypt_pwd = get_encrypt_pwd("testpwd")
    print(encrypt_pwd)
    get_auth_code()
