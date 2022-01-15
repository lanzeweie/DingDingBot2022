# -- coding: UTF-8 --
#抽取url 然后返回钉钉机器人
import requests
import re
import os
import sys

count = 0
shuzi_s = ['4kfengjing','4kmeinv','4kyouxi','4kdongman','4kyingshi','4kmingxing','4kqiche','4kdongwu','4krenwu','4kmeishi','4kzongjiao','4kbeijing']
#number = input("请选择分类(输入数字):\n1. 4k风景\n2. 4k美女\n3. 4k游戏\n4. 4k动漫\n5. 4k影视\n6. 4k明星\n7. 4k汽车\n8. 4k动物\n9. 4k人物\n10. 4k美食\n11. 4k宗教\n12. 4k背景\n")
number = sys.argv[1]
weizhi = os.path.dirname(os.path.abspath(__file__))

#判断是否是特定的文字  并转换数字
def panduan():
   global shuzi
   try:
      if number in "风景图":
         shuzi = 1
      if number in "妹子图":
         shuzi = 2
      if number in "游戏图":
         shuzi = 3
      if number in "动漫图":
         shuzi = 4
      if number in "电影图":
         shuzi = 5
      if number in "明星图":
         shuzi = 6
      if number in "跑车图":
         shuzi = 7
      if number in "动物图":
         shuzi = 8
      if number in "人物图":
         shuzi = 9
      if number in "美食图":
         shuzi = 10
      if number in "宗教图":
         shuzi = 11
      if number in "背景图":
         shuzi = 12
      baba = shuzi
   except:
      print("no")
      os._exit(0)

#抽奖
def PICbian():
    #从小程序爬取的 url 中随机抽取url
    #格式化文本
    import random
    file = open(weizhi+'/img/'+shuzi_s[int(shuzi) - 1]+'.txt',encoding='UTF-8')
    lines = file.readlines()
    urlPIC1=[]
    for urlPIC2 in lines:
    	temp=urlPIC2.replace('\n','')
    	urlPIC1.append(temp)
    #随机抽取一个
    urlPIC3 = random.choice(urlPIC1)
    #第二种抽法
    #urlPIC = (str(urlPIC3).strip().strip('''"'[]'"'''))
    sendText = "![彼岸网]("+urlPIC3+")"
    print(sendText)

panduan()

if len(str(shuzi))>0:
   PICbian()
else:
   pass