#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
#python 3.8
import time
import hmac
import hashlib
import base64
import urllib.parse
#暂存信息
import configparser
import os
import sys


#钉钉机器人配置信息
timestamp = str(round(time.time() * 1000))
secret = 'SECca2c9a388c1bed9c0702e6ed3d3e37ea9c5dc7751a9324fd87c9c9bfe0a708b6'
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
url='https://oapi.dingtalk.com/robot/send?access_token=39b8bf54bda1b89f88e4ab4ff2b15e978ffde50d1b5fd76616ce3989c51458d4&timestamp={}&sign={}'.format(timestamp, sign)
uid = '$:LWCP_v1:$lKh6TGW/6XEyY3Ho0ZAreuvmhpvC3H/R'

class DingBot():
    def __init__(self,Send):
        self.Send = Send
        
        

    def DingSend(self):
            #钉钉信息配置
        headers={
        'Content-Type':'application/json'
        }
        json={"msgtype": "text",
            "text": {
                "content":self.Send
            },
            "at": {
                "atDingtalkIds": [
                    uid
                ],
                "isAtAll": False
            }
        }
        resp=requests.post(url=url,headers=headers,json=json)