# -- coding:utf-8 --
#项目接口
#sys.path.append(start_lu)  如果导入私包 需要加环境变量
import configparser
import datetime
import os
import sys
import time

start_lu = os.path.dirname(os.path.abspath(__file__))

class project_public():
    def __init__(self, post_userid, post_mes) -> str:
        self.post_userid = post_userid
        self.post_mes = post_mes
class project_private():
    def __init__(self, post_userid, post_mes) -> str:
        self.post_userid = post_userid
        self.post_mes = post_mes
 
    class Birtday():
        def __init__(self, post_userid, post_mes) -> str:
            self.post_userid = post_userid
            self.post_mes = post_mes
    #生日查询项目
        def Birthday_help(self):
            message = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "|🎂Birthday🎂|",
                    "text": "# **🎂Birthday功能 帮助🎂** \n\n ## **查询某月有哪些人过生日** \n\n >@私人助手 查询X月生日 \n\n ## **查询所有月** \n\n >@私人助手 查询所有月生日 \n\n-------------------\n\n >@私人助手 查询XXX的生日 \n\n-------------------\n\n 默认功能 不需要手动启动 \n\n 每月月初会发送当月过生日的人数 \n\n 如果某人还有10天过生日则每日提醒"
                },
                "at": {
                    "atDingtalkIds": [self.post_userid],
                    "isAtAll": False
                }
            }
            return message
        def Birthday_Send(self):
            sys.path.append(start_lu) 
            from app.Birthday.main.Birthday_query import BirthdayQuery
            if int(self.post_mes) > 0 and int(self.post_mes) < 13:
                #开始执行查询命令
                Birthday_Send = BirthdayQuery.Birthday_date_text(self.post_mes)
                message = {
                    "msgtype": "text",
                    "text": {
                        "content": '|🎂生日提醒小助手🎂|\n'+Birthday_Send
                    },
                    "at": {
                        "atDingtalkIds": [self.post_userid],
                        "isAtAll": False
                    }
                }
                return message
        def Birthday_all_Send(self):
            sys.path.append(start_lu) 
            from app.Birthday.main.Birthday_query import BirthdayQuery
            Birthday_all_Send = ""
            for moth in range(12):
                Birthday_all_text = BirthdayQuery.Birthday_date_text(moth)
                Birthday_all_Send += Birthday_all_text
            message = {
                "msgtype": "text",
                "text": {
                    "content": '|🎂生日提醒小助手🎂|\n'+Birthday_all_Send
                },
                "at": {
                    "atDingtalkIds": [self.post_userid],
                    "isAtAll": False
                }
            }
            return message
        def Birthday_appoint(self):
            sys.path.append(start_lu) 
            from app.Birthday.main.Birthday_query import BirthdayQuery
            
            date = BirthdayQuery.Birthday_appoint(self.post_mes)
            if date is None:
                send_mes = '没有该用户'
                return project_private.gongyong.sendText(self.post_userid, send_mes)
            else:
                message = {
                    "msgtype": "text",
                    "text": {
                        "content": '|🎂生日提醒小助手🎂|\n'+self.post_mes+'的生日是\n'+date
                    },
                    "at": {
                        "atDingtalkIds": [self.post_userid],
                        "isAtAll": False
                    }
                }
                return message

        def Birtday_mlh(self):
            sys.path.append(start_lu) 
            from app.Birthday.Birthday_mlh import Birthdaymlh
            markdownpd = (Birthdaymlh(self.post_mes[6:]).mlh())
            try:
                if markdownpd[0] == "help":
                    message = {
                        "msgtype": "markdown",
                        "markdown": {
                            "title": "|🎂Birthday mlh🎂|",
                            "text": markdownpd[1]
                        },
                        "at": {
                            "atDingtalkIds": [self.post_userid],
                            "isAtAll": False
                        }
                    }
                    return message
            except:
                pass
            return project_private.gongyong.sendText(self.post_userid,markdownpd)

    class gongyong():
        def sendText(post_userid, send_mes):
            # 发什么回复什么
            message = {
                "msgtype": "text",
                "text": {
                    "content": send_mes
                },
                "at": {
                    "atDingtalkIds": [post_userid],
                    "isAtAll": False
                }
            }
            return message

if __name__ == "__main__":
    print(project_public("$:LWCP_v2:$lKh6TGW/6XEyY3Ho0ZAreuvmhpvC3H/R","周锦涵").jieluloser())