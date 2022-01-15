
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:32:25 2020
@author: ydc
"""
#百度图片搜索
#魔改 https://blog.csdn.net/qq_40774175/article/details/81273198 后 接入钉钉机器人 的小程序内 2021.4.22
 
 
import re
import requests
from urllib import error
from bs4 import BeautifulSoup
import os

#存档
import json
import configparser
import sys

num = 0
numPicture = 0
List = []

#配置
baidu_soutu_w_1 = os.path.dirname(os.path.abspath(__file__))
baidu_soutu_w = configparser.ConfigParser()


#接入钉钉信息
baidu_soutu_l = sys.argv[1]

#检测必备文件是否存在
baidu_soutu_w_txt_1 = os.path.dirname(os.path.abspath(__file__))
baidu_soutu_w_txt = baidu_soutu_w_txt_1+"/url.txt"
with open(baidu_soutu_w_txt, "w+", encoding='utf-8') as outfile:
    outfile.truncate(0)


def Find(url, A):
    global List
    #print('正在检测图片总数，请稍等.....')
    t = 0
    i = 1
    s = 0
    while t < 10:
        Url = url + str(t)
        try:
            # 这里搞了下
            Result = A.get(Url, timeout=7, allow_redirects=False)
        except BaseException:
            t = t + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  # 先利用正则表达式找到图片url
            s += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                t = t + 60
    return s
 
 
def recommend(url):
    Re = []
    try:
        html = requests.get(url, allow_redirects=False)
    except error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        div = bsObj.find('div', id='topRS')
        if div is not None:
            listA = div.findAll('a')
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())
        return Re
 
 
def dowmloadPicture(html, keyword):
    global num
    # t =0
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  # 先利用正则表达式找到图片url
    #print('找到关键词:' + keyword + '的图片，即将开始下载图片...')
    for each in pic_url:
        #print('正在下载第' + str(num + 1) + '张图片，图片地址:' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
                #改
                with open(baidu_soutu_w_1+"/url.txt","a+") as f:
                    f.write(str(each)+"\n")  
            else:
                continue
        except BaseException:
            #print('错误，当前图片无法下载')
            continue
        else:
            num += 1
        if num >= numPicture:
            return
 
 
if __name__ == '__main__':  # 主函数入口
 
##############################
    # 这里加了点
    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
        'Upgrade-Insecure-Requests': '1'
    }
 
    A = requests.Session()
    A.headers = headers
###############################
 
    word = baidu_soutu_l
    # add = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=%E5%BC%A0%E5%A4%A9%E7%88%B1&pn=120'
    url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&pn='
 
    # 这里搞了下
    tot = Find(url, A)
    Recommend = recommend(url)  # 记录相关推荐
    #print('经过检测%s类图片共有%d张' % (word, tot))
    numPicture = 10
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
 
            # 这里搞了下
            result = A.get(url, timeout=10, allow_redirects=False)
        except error.HTTPError as e:
            #print('网络错误，请调整网络后重试')
            t = t + 60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60
 
    #print('当前搜索结束，感谢使用')
    #print('猜你喜欢')
    for re in Recommend:
        pass
        #print(re, end='  ')