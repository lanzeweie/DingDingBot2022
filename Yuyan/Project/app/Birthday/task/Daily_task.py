# -*- coding:utf-8 -*-
#生日查询 每日启动
#简介
#生日大于10天则不输出内容
#如果生日小于10天则每日输出
import datetime
import os
weizhi = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

now_month = datetime.datetime.now().strftime("%m")
now_day = datetime.datetime.now().strftime("%d")

#启动程序
os.popen(f'python3 {weizhi}/Query.py {now_month}','w')

#防止出现 13月的问题
month_13 = int(now_month) + 1
#判断今天是几日 如果日数大于等于 25 则把下个月一起查询了
if int(now_day) >= 25 and month_13 != 13:
    next_month = int(now_month) + 1
    os.popen(f'python3 {weizhi}/Query.py {next_month}','w')
#如果是12月 则查询1月
elif month_13 == 13:
    os.popen(f'python3 {weizhi}/Query.py 1','w')
    
