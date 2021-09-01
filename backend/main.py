#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : main.py
# @Author: SuperYong
# @Date  : 2021/9/19:55 下午
# @Desc  : FastApi main

import pymongo
from typing import List
from pydantic import HttpUrl
from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks

app = APIRouter()


