# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : common_utils.py
# @Author  : SuperYong
# @Date    : 2021/11/14 12:01 下午
# @Desc    :
from base64 import b64decode


def get_encrypt_decode(encrypt_code: str):
    """
    decode the encrypt
    :param encrypt_code:
    :return: timestamp, cipher
    """
    code_encode_utf8 = encrypt_code.encode('utf-8')
    code_b64decode = b64decode(code_encode_utf8).decode('utf-8')
    b64decode_split = code_b64decode.split('-')

    cipher = b64decode_split[1]
    timestamp = int(b64decode_split[0] + b64decode_split[2])

    return timestamp, cipher
