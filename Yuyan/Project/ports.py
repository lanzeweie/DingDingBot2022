# -- coding:utf-8 --
#项目接口
#sys.path.append(start_lu)  如果导入私包 需要加环境变量
import os,configparser,datetime,time,sys
start_lu = os.path.dirname(os.path.abspath(__file__))

class project_public():
    def __init__(self, post_userid, post_mes) -> str:
        self.post_userid = post_userid
        self.post_mes = post_mes

    class jielu():
        def __init__(self, post_userid, post_mes) -> str:
            self.post_userid = post_userid
            self.post_mes = post_mes

        def jieluloser(self,post_senderNick):
            sys.path.append(start_lu)
            #判断 时间是否在 凌晨 00:00 - 早上 7:30  如果在其中就让那天不记
            
            jielu_jin = 0
            d_time = datetime.datetime.strptime(str(datetime.datetime.now().date())+'00:00', '%Y-%m-%d%H:%M')
            d_time1 =  datetime.datetime.strptime(str(datetime.datetime.now().date())+'7:30', '%Y-%m-%d%H:%M')
            n_time = datetime.datetime.now()
            if n_time > d_time and n_time<d_time1:
                jielu_jin = 1
            # jielu 重置
            jieluw = f"{start_lu}/app/self_discipline/zancun.ini"
            cf = configparser.ConfigParser()
            cf.read(jieluw,"utf-8")
            #查看是否有免死金牌
            try:
                miansi = int(cf.get(self.post_userid,"免死金牌"))
                if miansi >= 1:
                    miansi_int = miansi-1
                    cf.set(self.post_userid, "免死金牌",str(miansi_int))
                    jieluday = int(cf.get(self.post_userid,"天数"))
                    cf.write(open(jieluw, "r+", encoding="utf-8"))
                    message = {
                        "msgtype": "text",
                        "text": {
                            "content": "你怎么可以这样！\n你明明已经坚持了 "+str(jieluday)+" 天！\n 你居然想毁掉自己的坚持,这次就当坚持了这么多天的奖励,忽略不计\n请继续坚持下去！！"
                        },
                        "at": {
                            "atDingtalkIds": [self.post_userid],
                            "isAtAll": False
                        }
                    }
                    return message
            except:
                pass
            cf.set(self.post_userid, "重置","1")
            if jielu_jin == 1:
                cf.set(self.post_userid, "当日","1")
            else:
                cf.set(self.post_userid, "当日","0")
            cf.write(open(jieluw, "r+", encoding="utf-8"))
            jieluwlu = f"{start_lu}/app/self_discipline/linshi/uid.ini"
            cf1 = configparser.ConfigParser()
            cf1.read(jieluwlu,"utf-8")
            cf1.set("lin", "uid",self.post_userid)
            cf1.write(open(jieluwlu, "r+", encoding="utf-8"))
            zuigaoday = int(cf.get(self.post_userid,"最高"))
            jieluday = int(cf.get(self.post_userid,"天数"))
            if jieluday > zuigaoday:
                cf.set(self.post_userid, "最高",str(jieluday))
                cf.write(open(jieluw, "r+", encoding="utf-8"))
            from app.self_discipline.discipline_passive import discipline_bianliang
            message = discipline_bianliang.loser(post_senderNick)
            return message
        def jieluhelp(self):
            # jielu 帮助
            message = {
                "msgtype": "markdown",
                "markdown": {
                    "title": "No🈲Male masturbation🈲No",
                    "text": "# **👶Jielu 帮助👶** \n\n ## **我该如何加入？** \n\n >@私人助手 加入戒撸计划 \n\n ## **我失败了该如何重来？** \n\n >@私人助手 戒撸失败请求重来 \n\n ## **我想知道我戒撸多久了** \n\n >@私人助手 我戒撸多久了 \n\n\n\n 第一次加入即算一天 \n\n 会在每天的7.30分进行打卡记录 \n\n-------------------\n\n 遇到好康的事物,请只欣赏她的美 \n\n **精虫**上脑请立即坐立 \n\n **精虫**完全上脑请立即到他人身旁 \n\n 戒撸非戒色,锻炼强大的自制力 \n\n 一天又一天的坚持下来,这里会陪伴着你  \n\n 加油( •̀ ω •́ )y"
                },
                "at": {
                    "atDingtalkIds": [self.post_userid],
                    "isAtAll": False
                }
            }
            return message
        def jielucx(self):
            # jielu查询
            jieluw = f"{start_lu}/app/self_discipline/zancun.ini"
            cf = configparser.ConfigParser()
            cf.read(jieluw,"utf-8")
            jieluday = int(cf.get(self.post_userid,"天数"))
            daystart = str(cf.get(self.post_userid,"开始日"))
            zuigaoday = int(cf.get(self.post_userid,"最高"))
            daynow = datetime.datetime.now().strftime('%Y年-%m月-%d日 %H:%M')
            message = {
                "msgtype": "text",
                "text": {
                    "content": "你已经在不撸的生活里度过 "+str(jieluday)+" 天啦！\n "+str(daystart)+" - "+str(daynow)+" \n最多坚持了 "+str(zuigaoday)+" 天 \n要加油一直坚持下去哦 \n h(￣▽￣)h😚"
                },
                "at": {
                    "atDingtalkIds": [self.post_userid],
                    "isAtAll": False
                }
            }
            return message
        def jielugo(self,post_userIds,post_senderNick):
            # jielu创建用户   需要附带  用户的个人id
            jieluwl = f"{start_lu}/app/self_discipline/zancun.ini"
            jielugo = configparser.ConfigParser()
            jielugo.read(jieluwl,"utf-8")

            #查看ini是否有此用户
            #uidy = ("'" + str(post_userid) + "'") 
            uidy = self.post_userid

            #如果有
            #if (uidy in str(cf.options("renyuan"))):#这是利用元素来判断，但是它不分大小写 
            if (uidy in str(jielugo.sections())):   #利用组名判断
                message = {
                    "msgtype": "text",
                    "text": {
                        "content": "你已经加入过计划啦，请不要重复加入哦(●ˇ∀ˇ●)"
                    },
                    "at": {
                        "atDingtalkIds": [self.post_userid],
                        "isAtAll": False
                    }
                }
                return message
            
            #没有则加入计划
            else:
                print("用户不在,即将构建")

                jielugo.add_section(self.post_userid)
                jielugo.set(self.post_userid, "天数", "0")
                daynow = datetime.datetime.now().strftime('%Y年-%m月-%d日 %H:%M')
                jielugo.set(self.post_userid, "开始日", daynow)
                jielugo.set(self.post_userid, "重置","0")
                jielugo.set(self.post_userid, "最高","0")
                jielugo.set(self.post_userid, "当日","0")
                jielugo.set(self.post_userid, "保护天数","0")
                jielugo.set(self.post_userid, "私ID",post_userIds)
                jielugo.write(open(jieluwl, "r+", encoding="utf-8"))
                time.sleep(2)
                message = {
                    "msgtype": "text",
                    "text": {
                        "content": "已经为你加入计划啦，今后的日子我会一直陪伴着你哦！😊"
                    },
                    "at": {
                        "atDingtalkIds": [self.post_userid],
                        "isAtAll": False
                    }
                }
                
                #存入uid.ini ，转接给discipline_passive
                jieluwlu = f"{start_lu}/app/self_discipline/linshi/uid.ini"
                jielugo_1 = configparser.ConfigParser()
                day_now_join = datetime.datetime.now().strftime('%Y年-%m月-%d日 %H:%M')
                with open(f"{start_lu}/app/self_discipline/logs/jielu.log","a",encoding="utf-8") as rizhi:
                    rizhi.write(f"[{day_now_join}]\n用户名称：{post_senderNick}\n用户私ID：{post_userIds}\n加入戒撸计划\n")
                try:
                    jielugo_1.read(jieluwlu,"utf-8")
                except:
                    print("奇怪的错误")

                #启动discipline_passive
                os.system(f"python3 {start_lu}/app/self_discipline/discipline_passive")
                return message

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