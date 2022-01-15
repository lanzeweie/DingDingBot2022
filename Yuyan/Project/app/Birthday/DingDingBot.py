#!/usr/bin/python
# -*- coding: UTF-8 -*-
#单独消息模块 由其他程序调用
import requests,json,os
shangji_lujin = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../.."))
weizhi = os.path.dirname(os.path.abspath(__file__))
#python 3.8
class DingBot():
    def __init__(self,Send):
        self.Send = Send
    
    def DingDing_single(json,accessToken):
        #配置
        url = "https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend"
        head = {
            "Host":"api.dingtalk.com",
            "x-acs-dingtalk-access-token":accessToken,
            "Content-Type":"application/json"
        }

        ione = requests.post(url,headers=head,json=json)
        print(ione.text)
        return ione.text
        
    def DingDing_single_accessToken():
        url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
        head = {
            "Host":"api.dingtalk.com",
            "Content-Type":"application/json"
        }
        body = {
            "appKey":AppKey_set,
            "appSecret":AppSecret_set
        }
        ba =requests.post(url,headers=head,json=body)
        ba_json = json.loads(ba.text)
        ba_json_ues = (ba_json['accessToken'])
        return ba_json_ues

    def DingDingSet():
        with open(f"{shangji_lujin}/data/DingDingSet.json","r",encoding="utf-8") as set:
            DingSet = set.read()
        global Webhook_set,AppSecret_set,AppKey_set
        DingSet_text = eval(DingSet)
        Webhook_set = (DingSet_text['set'][0]['Webhook'])
        AppSecret_set = (DingSet_text['set'][0]['AppSecret'])
        AppKey_set = (DingSet_text['set'][0]['AppKey'])

    def main(self):
        DingBot.DingDingSet()
        with open(weizhi+"/json/Birthday.json","r",encoding="utf-8") as f:
            B_date_text = f.read()
        B_date_json = json.loads(B_date_text)
        userIds = (B_date_json['list'][0]['userIds'])

        accessToken = DingBot.DingDing_single_accessToken()
        DingDing_single_xiaoxiti_msgParam_bianliang = ({"content":self.Send})
        DingDing_single_xiaoxiti_json = {
        "robotCode" : AppKey_set,
        "userIds" : [ userIds ],
        "msgKey" : "sampleText",
        "msgParam" : ''+str(DingDing_single_xiaoxiti_msgParam_bianliang)+''
        }
        DingBot.DingDing_single(DingDing_single_xiaoxiti_json,accessToken)

if __name__ == "__main__":
    DingBot("你好").main()

    #如果需要单独使用的话, 修改 shangji_lujin 对应的路径,否则只能在当前文件路径使用
    #程序原理
    #带参数启动  main() ➡ 启动 ➡ DingBot.DingDingSet() ➡ 获取配置信息 ➡ main()继续启动 DingDing_single_accessToken() ➡ 获取accessToken 码 ➡ 再启动 DingDing_single 发给钉钉
