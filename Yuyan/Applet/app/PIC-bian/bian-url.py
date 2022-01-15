# -- coding: UTF-8 --
import requests
import re
import os
import sys

#魔改 https://github.com/GOODBOY-YJH/pixiv-picture-downloader   接入钉钉机器人 2021.4.30  21:07
#彼岸网更新程序 请启动 start-bianan.py

count = 0
select_s = ['4kfengjing','4kmeinv','4kyouxi','4kdongman','4kyingshi','4kmingxing','4kqiche','4kdongwu','4krenwu','4kmeishi','4kzongjiao','4kbeijing']
#number = input("请选择分类(输入数字):\n1. 4k风景\n2. 4k美女\n3. 4k游戏\n4. 4k动漫\n5. 4k影视\n6. 4k明星\n7. 4k汽车\n8. 4k动物\n9. 4k人物\n10. 4k美食\n11. 4k宗教\n12. 4k背景\n")
number = sys.argv[1]
weizhi = os.path.dirname(os.path.abspath(__file__))

def getHTMLText(url):#获取页面信息
   try:
        kv = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        r = requests.get(url, timeout = 10, headers = kv)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
   except:
        return '获取页面错误'
       

def ParsePage(ilt, html): #把每一个网页里对应的图片下载出来
   try:
       imag_s = re.findall(r'img src=\"/[a-z]+/[a-z]+/[0-9]+/[0-9]+-[\w]+\.jpg\" data',html)
       imags = 'https://pic.netbian.com' + imag_s[0].split('"')[1]
       ilt.append(imags)
   except:
       print('')

def ParsePage_1(ilt, html):#把主页面的每一张带图片的网页链接找出来
   try:
       imag_s = re.findall(r'a href=\"/tupian/[\d]+\.html\" target',html)
       for im in range(len(imag_s)):
          imags = 'https://pic.netbian.com' + imag_s[im].split('"')[1]
          ilt.append([imags])
   except:
       print('')

def SaveImag(ilt):
   root = (weizhi+"/img/" + select_s[int(number) - 1]+".txt")
   for li in ilt:
      with open(root, "a+", encoding='utf-8') as gg:
         gg.write(str(li+"\n"))


def main():
   try:
      Url = ("https://pic.netbian.com/"+select_s[int(number) - 1])
      for i in range(5):  #1=20张
         imagList = []
         Html = getHTMLText(Url)    #解析每一页的所有图片链接
         ParsePage_1(imagList, Html)
         Url = str('https://pic.netbian.com/' + select_s[int(number) - 1] + '/index_' + str(i + 1)+ '.html') #新的一页
         for imag in imagList: #获得链接
            url = imag[0]
            infoList = []
            html = getHTMLText(url)
            ParsePage(infoList, html)
            SaveImag(infoList)
   except:
      pass

main()
#排除重复
end = (weizhi+"/img/" + select_s[int(number) - 1]+".txt")
cmd = os.popen('sort '+end+' |uniq').read()
with open(end,"w+") as f:
   f.write(str(cmd))