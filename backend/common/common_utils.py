# ！/usr/bin/env python
# -*- coding: utf-8 -*-
# @File    : common_utils.py
# @Author  : SuperYong
# @Date    : 2021/11/14 12:01 下午
# @Desc    :
from loguru import logger
from base64 import b64decode, b64encode
from fastapi import HTTPException, status
from common.schemas import RequestStatus


def get_encrypt_decode(encrypt_code: str):
    """
    decode the encrypt
    :param encrypt_code:
    :return: timestamp, cipher
    """
    try:
        logger.debug(encrypt_code)
        code_encode_utf8 = encrypt_code.encode('utf-8')
        code_b64decode = b64encode(code_encode_utf8).decode('utf-8')
        logger.debug(code_b64decode)
        b64decode_split = code_b64decode.split('-')
        logger.debug(b64decode_split)
        cipher = b64decode_split[1]
        timestamp = int(b64decode_split[0] + b64decode_split[2])
    except Exception as e:
        logger.error(e)
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail={'status': RequestStatus.error, 'msg': "input code error!"},
            headers={"WWW-Authenticate": "Bearer"},
        )

    return timestamp, cipher
