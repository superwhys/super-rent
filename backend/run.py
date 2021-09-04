#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: SuperYong
# @Date  : 2021/9/412:16 上午
# @Desc  :

import uvicorn
from main import app
from fastapi import FastAPI

Applications = FastAPI(
    title='Super Rent API Docs',
    description='Super Rent 租金管理平台API接口文档',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redocs',
)


Applications.include_router(app, prefix='/rent', tags=['API接口'])


if __name__ == '__main__':
    uvicorn.run('run:Applications', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
