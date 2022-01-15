# -*- coding:utf-8 -*-
#由外部程序启动
#获取即将过生日的人json信息 并转换成文本 由钉钉输出
#参数从Birthday_news.json读取
import os
import datetime
import sys
path = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
sys.path.append(path) 
from DingDingBot import DingBot
weizhi = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

#初始化
with open(weizhi+"/json/Birthday_news.json","r",encoding="utf-8") as news:
    Birthday_news_text = news.read()
Birthday_news_json = eval(Birthday_news_text)
Birthday_news_len = len(Birthday_news_json)
mother = datetime.datetime.now().strftime("%m")

#输出信息
#模板  Birthday_news_len-1  是因为为了方便读取列表额外添加了一个{name,End} 所以需要减去这个
Send = (f"|🎂生日提醒小助手🎂|\n最近10天内\n有{Birthday_news_len-1}位朋友过生日哦\n--------寿星---------\n")

#判断传送了多少个列表参数 并执行多少次
for shu in range(Birthday_news_len):
    name = Birthday_news_json[shu]['name']
    if name == 'End':
        continue
    date = Birthday_news_json[shu]['date']
    year = Birthday_news_json[shu]['year']
    countdown = Birthday_news_json[shu]['countdown']
    if countdown == '0':
        Birthday_news_Send = (f"🎂🎂🎂🎂🎂🎂🎂🎂\n{name}\n {date}\n今天是ta的{year}岁生日哦\n🎂🎂🎂🎂🎂🎂🎂🎂-------------------\n")
    elif countdown != '0':
        Birthday_news_Send = (f"{name} 今年{year}岁\n {date}\n还有{countdown}天过生日\n-------------------\n")
    Send += Birthday_news_Send
Send += ("一定要记得给他们祝福哦")

#DingBot.DingSend(Send)
#Send = (Send.encode('utf-8'))
DingBot(Send).main()