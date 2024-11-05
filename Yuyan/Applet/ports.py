# -- coding:utf-8 --
#小程序接口
import os,requests,json,random,sys
start_lu = os.path.dirname(os.path.abspath(__file__))
sys.path.append(start_lu)
#接入小程序的接口
from Applet.app.xiaomi.ports import xiaomiyundong_chushi
from Applet.app.weather.ports import weather_query
from Applet.app.Chat.OpenAi.chatgpt import ChatgptDL,ChatgptQUN
#公共的小程序接口
class applet_public():
    def __init__(self,post_userid, post_mes, post_userIds, post_senderNick, post_isAdmin):
        self.post_userid = post_userid
        self.post_mes = post_mes
        self.post_userIds = post_userIds
        self.post_senderNick = post_senderNick
        self.post_isAdmin = post_isAdmin

    def appHMACGurl(self):
        #幻猫小程序
        #app-HM-ACG-url #小程序 根据 幻猫爬虫抓取的 url 随机发送一个url
        #格式化文本
        file = open(f'{start_lu}/app/HM-ACG-url/url.txt',encoding='UTF-8')
        lines = file.readlines()
        urlHM1=[]
        for urlHM2 in lines:
            temp=urlHM2.replace('\n','')
            urlHM1.append(temp)
        #随机抽取一个
        urlHM3 = random.choice(urlHM1)
        #urlHM = (str(urlHM3).strip().strip('''"'[]'"'''))

        #投入发送
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title":"幻猫ACG美图一张",
                "text": "![幻猫ACG]("+(str(urlHM3).strip().strip('''"'[]'"'''))+")"
            },
            "at": {
                "atDingtalkIds": [],
                "isAtAll": False
            }
        }
        return message
    def appHMACGurlUP(self):
        #管理员
        #启动小程序 幻猫ACG的爬虫更新程序
        print("管理员命令：更新幻猫ACG图片")
        os.system(f"python3 {start_lu}/app/HM-ACG-url/start-url.py")
        #计算url行数 = 多少张图
        url_hang = -1
        for url_hang, line in enumerate(open("./app/HM-ACG-url/url.txt", 'r', encoding='UTF-8')):
            pass
        url_hang += 1

        #发送
        message = {
            "msgtype": "text",
            "text": {
                "content": "已经成功更新幻猫ACG近期的图片啦♪(^∇^*),现在列表里一共有 "+str(url_hang)+"张 图片哦"
            },
            "at": {
                "atDingtalkIds": [self.postuserid],
                "isAtAll": False
            }
        }
        return message
    def appHMACGhelp(self):
        # 幻猫网 帮助
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": "幻猫网食用指南(●ˇ∀ˇ●)",
                "text": "# **💁幻猫网小程序 帮助💁** \n **我该如何使用？** \n\n >@私人助手 发一张幻猫的cos图 \n\n **简介一点** \n\n >@私人助理 发张cos图 \n\n-------------------\n\n **我是管理员如何更新图库？** \n\n >@私人助手 更新幻猫网"
            },
            "at": {
                "atDingtalkIds": [self.post_userid],
                "isAtAll": False
            }
        }
        return message
    
    def appWeather(self, post_mes_weather):
        #天气小程序
        #过滤信息 获得城市名字
        #启动weather小程序,传递变量 并获得输出
        cmd = weather_query.query(post_mes_weather)

        #发送
        message = {
            "msgtype": "text",
            "text": {
                "content": cmd
            },
            "at": {
                "atDingtalkIds": [self.post_userid],
                "isAtAll": False
            }
        }
        return message

    def appBaidusoutu(post_userid, post_mes_baidusoutu):
        #启动百度搜图小程序附带变量
        os.system(f"python3 {start_lu}/app/BaiDu-Soutu/baidu_soutu.py "+post_mes_baidusoutu)
        #os.popen('python3 ./app/BaiDu-Soutu/baidu_soutu.py')

        #根据 百度搜图小程序获得的图片 随机抽选一张发送
        #格式化文本
        import random
        file = open(f'{start_lu}/app/BaiDu-Soutu/url.txt',encoding='UTF-8')
        lines = file.readlines()
        urlBDST1=[]
        for urlBDST2 in lines:
            temp=urlBDST2.replace('\n','')
            urlBDST1.append(temp)
        #随机抽取一个
        urlBDST3 = random.choice(urlBDST1)

        #投入发送
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title":"百度搜图成功啦",
                "text": "![百度图片]("+str(urlBDST3)+")"
            },
            "at": {
                "atDingtalkIds": [],
                "isAtAll": False
            }
        }
        return message

    def appPICbian(post_userid, post_mes_PICbian):
        #彼岸网小程序
        #发送给 bian-start-url.py 并获得信息
        cmd = os.popen(f'python3 {start_lu}/app/PIC-bian/bian-start-url.py '+post_mes_PICbian).read()
        #是否返回正确值
        if len(cmd)>0:
            #返回
            message = {
                "msgtype": "markdown",
                "markdown": {
                    "title":"随机彼岸网图片一张🤭",
                    "text": cmd
                },
                "at": {
                    "atDingtalkIds": [],
                    "isAtAll": False
                }
            }
            return message
        else:
            send_mes = '''没有找到这种类型的图片哦，非常非常抱歉╥﹏╥...'''
            return gongyong.sendText(post_userid, send_mes)
    def appPICbianUP(post_userid):
        #管理员
        #启动PICbiana更新小程序,并获得输出
        cmd = os.popen(f'python3 {start_lu}/app/PIC-bian/start-bian.py').read()

        #发送
        message = {
            "msgtype": "text",
            "text": {
                "content": cmd
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message
    def appPICbianhelp(post_userid):
        # 彼岸网 帮助
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": "彼岸网食用指南(●ˇ∀ˇ●)",
                "text": "# **💁彼岸网小程序 帮助💁** \n **我该如何使用？** \n\n >@私人助手 发一张彼岸网的(XX)图 \n\n **(XX)可以是哪些？** \n\n >风景 妹子 游戏 动漫 电影 明星 \n\n >跑车 动物 人物 美食 宗教 背景 \n\n-------------------\n\n **我是管理员如何更新图库？** \n\n >@私人助手 更新彼岸网"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message

    def appapipixivweb(post_userid):
        #随机二次元图片一张
        pixivweb_session = requests.Session()
        pixivweb = pixivweb_session.get("https://api.pixivweb.com/anime18r.php?return=json")
        pixivweb_js = json.loads(pixivweb.text)
        pixivweb_js_imgurl = pixivweb_js["imgurl"]
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": "随机二次元图片一张!",
                "text": "![随机二次元图片]("+str(pixivweb_js_imgurl)+")"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message

    def chatgpt(post_userIds, send_mes, post_senderNick, post_moshi):
        #2023/4/21 支持连续对话,单聊私人聊天记录，群聊共享聊天记录
        if post_moshi == "1":
            return ChatgptDL.init(post_userIds,post_senderNick,send_mes)
        elif post_moshi == "2":
            return ChatgptQUN.init(post_senderNick,send_mes)

#私人的小程序接口
class applet_private():
    def __init__(self,post_userid, post_mes, post_userIds, post_senderNick, post_isAdmin) -> str:
        self.post_userid = post_userid
        self.post_mes = post_mes
        self.post_userIds = post_userIds
        self.post_senderNick = post_senderNick
        self.post_isAdmin = post_isAdmin

    def siappxiaomibushu2d(self,xiaomi_bushu_bushu_surr):
        cmd = xiaomiyundong_chushi.start(self.post_userid,self.post_senderNick,xiaomi_bushu_bushu_surr)
        if cmd is None:
            cmd = "该用户未开通刷步数权限呢"
        message = {
            "msgtype": "text",
            "text": {
                "content": '⚽运动小助手⚽\n'+cmd
            },
            "at": {
                "atDingtalkIds": [self.post_userid],
                "isAtAll": False
            }
        }
        return message

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
