# coding=gbk
# @File  : run.py
# @Author: SuperYong
# @Date  : 2021/9/412:16 上午
# @Desc  :

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from user.user_app import user_app
from config import RUN_PORT, DOCS_DEBUG
from tenant.tenant_app import tenant_app
from baseApi.base_api import base_api_router
from unit_rent.unit_rent_app import unit_rent_app

from loguru import logger
from sys import stderr


logger.remove()
logger.add(stderr, level="DEBUG")


Applications = FastAPI(
    title='Super Rent API Docs',
    description='Super Rent 租金管理平台API接口文档',
    version='0.0.1',
    docs_url='/docs' if DOCS_DEBUG else None,
)

Applications.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Applications.include_router(base_api_router, prefix='/rent/v1')
Applications.include_router(user_app, prefix='/rent/v1', tags=['用户相关 API接口'])
Applications.include_router(tenant_app, prefix='/rent/v1', tags=['租客相关 API接口'])
Applications.include_router(unit_rent_app, prefix='/rent/v1', tags=['出租单位相关 API接口'])

if __name__ == '__main__':
    uvicorn.run('run:Applications', host='0.0.0.0', port=RUN_PORT, reload=True, debug=True, workers=4)
