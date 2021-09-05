# coding=gbk
# @File  : config.py
# @Author: SuperYong
# @Date  : 2021/9/311:02 下午
# @Desc  : const file

from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException, status
from passlib.context import CryptContext


'''FastAPI'''
RUN_PORT = 8000


'''databases'''
HOST = 'mongo'
PORT = 27017


SECRET_KEY = "fe8a711ed3fcc1ba9e56d35369ebc589bc420d6bf474eed24b878b7a09e9ed96"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/rent/user/login")

credentials_exception = HTTPException(
        status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )