#!/usr/bin/python
# -- coding: UTF-8 --
import time
import configparser
import os
import datetime
#主程序创建用户后使用此程序激活
#用户失败后使用此程序归零
#入口 discipline_bianliang.loser()

#获得当前变量用户信息
weizhi = os.path.dirname(os.path.abspath(__file__))
cb = configparser.ConfigParser()
cb.read(weizhi + "/linshi/uid.ini","utf-8")
uid = cb.get("lin","uid")
#暂存信息
rootPath = os.path.dirname(os.path.abspath(__file__))
cf = configparser.ConfigParser()
cf.read(rootPath + "/zancun.ini","utf-8")
day = int(cf.get(uid,"天数"))
day2 = str(cf.get(uid,"开始日"))
day3 = datetime.datetime.now().strftime('%Y年-%m月-%d日 %H:%M')

class discipline_bianliang():
    def DingDing_single_xiaoxiti_zhuanyi(send_mes):
        #回执消息
        #暂存本地ini
        day = int(cf.get(uid,"天数"))
        day += int(1)
        day1 = day
        cf.set(uid, "天数",str(+day1))
        cf.write(open(rootPath + "/zancun.ini", "r+", encoding="utf-8"))
        return send_mes 

    def loser(post_senderNick):
        #检查是否失败
        loser = int(cf.get(uid,"重置"))
        if loser==1:
            json={"msgtype": "text",
                "text": {
                    "content": str(day2)+" - "+str(day3)+" \n 你已经坚持 "+str(day)+" 天了 \n 虽然因为种种原因导致你中途放弃 \n 请不要自责！！\n 重组心态 坚持下去！！\n 戒掉这不良习惯！！！\n 加油！！！！"
                },
                "at": {
                    "atDingtalkIds": [
                        uid
                    ],
                    "isAtAll": False
                }
            }
            cf.set(uid, "天数","0")
            cf.set(uid, "开始日",str(day3))
            cf.set(uid, "重置","0")
            cf.write(open(rootPath + "/zancun.ini", "r+", encoding="utf-8"))
            with open(f"{weizhi}/logs/jielu.log","a",encoding="utf-8") as rizhi:
                rizhi.write(f"[{day3}]\n用户名称：{post_senderNick}\n戒撸失败\n")
            time.sleep(1)
            return discipline_bianliang.DingDing_single_xiaoxiti_zhuanyi(json)
        else:
            with open(f"{weizhi}/logs/jielu.log","a",encoding="utf-8") as rizhi:
                rizhi.write(f"[{day3}]\n用户名称：{post_senderNick}\n用户ID：{uid}\n加入戒撸计划\n")
            return discipline_bianliang.xin()

    def xin():
        #正常启动
        #天数
        day = int(cf.get(uid,"天数"))
        day += int(1)
        day1 = day

        #钉钉信息配置
        headers={
        'Content-Type':'application/json'
        }
        json={"msgtype": "text",
            "text": {
                "content":"👼健康生活👼 \n 恭喜你又又坚持了一天！！！\n 可喜可贺~可喜可贺 (∩_∩)  \n 新的一天也要坚持下去哦！\n 加油加油(ง •_•)ง  \n-------------------\n " +str(day2)+" \n -----至----- \n "+str(day3)+" \n 至今你已经坚持了："+str(day1)+" 天 \n 请务必保持下去哦 o(*￣▽￣*)o"
            },
            "at": {
                "atDingtalkIds": [
                    uid
                ],
                "isAtAll": False
            }
        }
        return discipline_bianliang.DingDing_single_xiaoxiti_zhuanyi(json)



if __name__ == "__main__":
    print(discipline_bianliang.loser())    
