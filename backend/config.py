# coding=gbk
# @File  : config.py
# @Author: SuperYong
# @Date  : 2021/9/311:02 ����
# @Desc  : const file

from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext


SECRET_KEY = "fe8a711ed3fcc1ba9e56d35369ebc589bc420d6bf474eed24b878b7a09e9ed96"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/rent/user/login")
