#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : descriptions.py
# @Author: SuperYong
# @Date  : 2021/9/511:54 下午
# @Desc  : Api descriptions


"""unit_rent_app description"""
get_unit_rent_desc = '参数：无, 需在headers中携带登录后的token, 字段为Authorization'
get_unit_rent_info_desc = '参数：rent_name -> 出租单位名称, 需在headers中携带登录后的token, 字段为Authorization'


"""user description"""
login_desc = 'POST请求, 参数：用户名和密码'
register_desc = 'POST请求, 参数: 用户名, 密码, 权限, 手机号'


"""tenant description"""
create_tenant_desc = 'POST请求, 参数: 租客名 出租单位(可选) 出租单元(可选) 租期状态(可选) 计划租房月数(可选) 电话 身份证'
get_tenant_info_desc = "GET请求, 参数: 租客名 出租单位 出租单元"
