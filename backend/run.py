#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run.py
# @Author: SuperYong
# @Date  : 2021/9/412:16 上午
# @Desc  :

import uvicorn
from main import app
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


Applications = FastAPI(
    title='Super Rent API Docs',
    description='Super Rent 租金管理平台API接口文档',
    version='0.0.1',
    docs_url='/docs',
    redoc_url='/redocs',
)
"No 'Access-Control-Allow-Origin' header is present on the requested resource."
Applications.add_middleware(
    CORSMiddleware,
    allow_origins=[
        'http://127.0.0.1',
        'http://127.0.0.1:8000',
        'http://localhost:8080'
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Applications.include_router(app, prefix='/rent', tags=['API接口'])


if __name__ == '__main__':
    uvicorn.run('run:Applications', host='0.0.0.0', port=8000, reload=True, debug=True, workers=1)
