#-*- coding:utf-8 -*-
import os

#传参测试

userSend = '启动刷步数小程序,步数为:19301'

xiaomi_bushu_init = userSend[0:userSend.rfind(',')]
if (xiaomi_bushu_init == '启动刷步数小程序'):
    #内容判断
    xiaomi_bushu_bushu_init = userSend[userSend.rfind(':'):]
    #修改字符
    xiaomi_bushu_bushu_surr = xiaomi_bushu_bushu_init.replace(":","")
    print(xiaomi_bushu_bushu_surr)

cmd = os.popen('python3 ./updatabs.py '+xiaomi_bushu_bushu_surr).read()
print(cmd)