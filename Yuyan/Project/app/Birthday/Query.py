#!/usr/bin/python
# -*- coding: utf-8 -*-
#给程序传参 查询这个月有哪些人要过生日
#外部主要函数接口
#只输出 即将过生日的人
from main.Birthday_query import BirthdayQuery
from main.Birthday_judge import BirthdayJudge
import sys
import os
weizhi = os.path.dirname(os.path.abspath(__file__))
#初始化
mother = sys.argv[1]
judge = (BirthdayQuery.Birthday_date_json(mother))
judge += (',{"name":"End"}')
judge = eval(judge)
judge_len = len(judge)
Birthday_countdown = ""

#获取生日信息
for shu in range(judge_len):
    name = judge[shu]["name"]
    if name == 'End':
        continue
    date = judge[shu]["date"]
    day = BirthdayJudge(date).distance()[0]
    year = BirthdayJudge(date).distance()[1]
    #如果生日只差10天 则创建一个列
    if int(day) < 10 and int(day) >= 0:
        Birthday_countdown += ("{'name':'"+name+"','date':'"+date+"','countdown':'"+day+"','year':'"+year+"'},")
        #print(f"{name},还有{day}天到生日,今年{year}岁")

#判断列是否有元素 有就传参给消息提醒程序
Birthday_countdown_len = len(Birthday_countdown)
if Birthday_countdown_len != 0:
    #Birthday_countdown = Birthday_countdown[:-1]
    Birthday_countdown += ("{'name':'End'}")
    Birthday_countdown = Birthday_countdown.replace("'",'"')
    with open(weizhi+"/json/Birthday_news.json","w",encoding="utf-8") as nows:
        nows.write(Birthday_countdown)
    os.popen(f"python3 {weizhi}/task/Birthday_news.py","w")