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


if __name__ == '__main__':
    encrypt_pwd = get_encrypt_pwd("testpwd")
    print(encrypt_pwd)
