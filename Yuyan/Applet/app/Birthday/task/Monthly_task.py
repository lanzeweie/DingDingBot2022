# -*- coding:utf-8 -*-
#每月1号执行 查询这个月有那些人过生日
import datetime
import sys
import os
path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
sys.path.append(path) 
from main.Birthday_query import BirthdayQuery
from DingDingBot import DingBot

now_moth = datetime.datetime.now().strftime("%m")
Birthday = BirthdayQuery.Birthday_date_json(now_moth)

Birthday_news_json = eval(Birthday)
Birthday_news_len = len(Birthday_news_json)
#输出信息
#模板  Birthday_news_len-1  是因为为了方便读取列表额外添加了一个{name,End} 所以需要减去这个
Send = (f"|🎂生日提醒小助手🎂|\n*****现在是{now_moth}月*****\n有{Birthday_news_len}位朋友过生日哦\n--------寿星---------\n")

#判断传送了多少个列表参数 并执行多少次
for shu in range(Birthday_news_len):
    name = Birthday_news_json[shu]['name']
    if name == 'End':
        continue
    date = Birthday_news_json[shu]['date']
    Birthday_news_Send = (f"{name} {date}\n")
    Send += Birthday_news_Send
Send += ("-------------------\n一定要记得给他们祝福哦")

#DingBot.DingSend(Send)
#Send = (Send.encode('utf-8'))
DingBot(Send).DingSend()