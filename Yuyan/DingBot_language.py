# -- coding:utf-8 --
#钉钉机器人独立语言模块
import configparser,re,os,time,datetime,requests,json,sys
start_lu = os.path.dirname(os.path.abspath(__file__))
sys.path.append(start_lu)
print("\n开始进行 钉钉语言模块 初始化")
print("-------------------------------------------------------------------------")
from Applet.ports import applet_public,applet_private
print("\n钉钉语言模块 小程序 已接入完毕")
from Project.ports import project_public,project_private
print("\n钉钉语言模块 项目 已接入完毕")
from Applet.ports import applet_public,applet_private
from Project.ports import project_public,project_private



class DingDingLanguage():
    def __init__(self, post_userid, post_mes, post_userIds, post_senderNick, post_isAdmin):
        self.post_userid = post_userid
        self.post_mes = post_mes
        self.post_userIds = post_userIds
        self.post_senderNick = post_senderNick
        self.post_isAdmin = post_isAdmin
        
    def selectMes(self):
        applet_public_ports = applet_public(self.post_userid, self.post_mes, self.post_userIds, self.post_senderNick, self.post_isAdmin)
        applet_private_ports = applet_private(self.post_userid, self.post_mes, self.post_userIds, self.post_senderNick, self.post_isAdmin)
        #载入库存
        #信息
        #post_mes = 发送者信息
        #post_userid = 发送者ID
        #send_mes = 输出信息

        #获得 bot-multiple_messages/command_saemt.ini 配置信息 (全局变量) 手动配置
        bot_weizhi= f"{start_lu}/bot-multiple_messages/command_saemt.ini"
        bot_w = configparser.ConfigParser()
        bot_w.read(bot_weizhi,"utf-8")
        #具体bot信息配置  格式： eval(变量) 不然无法执行    mes代表普通消息 app代表小程序消息
        #普通消息
        bot_mes_jieshao = bot_w.get("all","jieshao_mes")
        #jielu-------------------------------------------------
        #jieluhelp 帮助
        bot_message_jieluhelp = bot_w.get("all", "jieluhelp")
        #jieluday 天数
        bot_message_jieluday = bot_w.get("all","jieluday")
        #jieluloser 重置
        bot_message_jieluloser = bot_w.get("all","jieluloser")
        #jielujihua 加入计划
        bot_message_jielujihua = bot_w.get("all","jielujihua")

        #app----------------------------------------------------
        #HM-ACG-jpg app-hmacgjpg   管理:app-hmacgjpg_up  非管理:app-hmacgjpg_up_no
        bot_message_app_hmacgjpg = bot_w.get("all", "app-hmacgjpg")
        bot_message_app_hmacgjpg_up = bot_w.get("all", "app-hmacgjpg_up")
        bot_message_app_hmacgjpg_up_no = bot_w.get("all", "app-hmacgjpg_up_no")
        #PIC-bian  管理:app-picbian_up  非管理:app-picbian_up_no
        bot_message_app_picbian_up = bot_w.get("all","app-picbian_up")
        bot_message_app_picbian_up_no = bot_w.get("all","app-picbian_up_no")
        bot_message_app_picbian = bot_w.get("all","app-picbian")
        #随机二次元图片 API提取
        bot_message_app_api_pixivweb = bot_w.get("all","apipixivweb")

        #钉钉机器人基层消息库 载入
        bot_say_ku = configparser.ConfigParser()
        bot_say_ku.read(f"{start_lu}/bot-multiple_messages/bot_message.ini","utf-8")
        #格式化
        bot_say_ku_linshi = bot_say_ku.sections()
        bot_say_ku_linshi_1 = bot_say_ku_linshi
        bot_say_ku_linshi_3=[]
        for bot_say_ku_linshi_2 in bot_say_ku_linshi_1:
            temp=bot_say_ku_linshi_2.replace('\n','')
            bot_say_ku_linshi_3.append(temp)

        #钉钉手动配置的消息判断
        if (self.post_mes == '你好'):
            send_mes = '你好啊朋友(*^_^*)!'
            return DingDingLanguage.sendText(self.post_userid, send_mes)
        if (self.post_mes == '你是谁'):
            send_mes = '我是周爸爸的小可爱😔~~'
            return DingDingLanguage.sendText(self.post_userid, send_mes)
        #普通消息 长信息
        if (eval(bot_mes_jieshao)):
            return DingDingLanguage.BotMesJiaoshao(self.post_userid)
        #Jielu  
        if (eval(bot_message_jieluhelp)):
            return project_public.jielu(self.post_userid,None).jieluhelp()
        if (eval(bot_message_jieluloser)):
            return project_public.jielu(self.post_userid,None).jieluloser(self.post_senderNick)
        if (eval(bot_message_jieluday)):
            return project_public.jielu(self.post_userid,None).jielucx()
        if (eval(bot_message_jielujihua)):
            return project_public.jielu(self.post_userid,None).jielugo(self.post_userIds,self.post_senderNick)

        #app-----------------------------------------------------------------------------------
        #HM-ACG-url 带管理
        if (eval(bot_message_app_hmacgjpg)):
            return applet_public_ports.appHMACGurl()
        if (eval(bot_message_app_hmacgjpg_up)):
            return applet_public_ports.appHMACGurlUP()
        if (eval(bot_message_app_hmacgjpg_up_no)):
            send_mes = '''你没有权力哦,只有我的周爸爸可以命令我干这种事情哦(●'◡'●)'''
            return DingDingLanguage.sendText(self.post_userid, send_mes)
        if (self.post_mes == "幻猫网帮助"):
            return applet_public_ports.appHMACGhelp()

        #weather 天气 把用户词汇分开进行判断
        #关键词天气 #如果分析除天气 则开始下一步地区判断
        weather_app_panduan_ci = self.post_mes[self.post_mes.rfind('天'):]
        if (weather_app_panduan_ci == '天气'):
            #地区
            self.post_mes_weather = self.post_mes[0:self.post_mes.rfind('天')]
            return applet_public_ports.appWeather(self.post_userid,self.post_mes_weather)

        #baidu_soutu 百度图片搜索 
        baidu_soutu_app_ci = self.post_mes[0:self.post_mes.rfind(':')]
        if (baidu_soutu_app_ci == '百度搜图'):
            #内容判断
            self.post_mes_baidusoutu = self.post_mes[self.post_mes.rfind(':'):]
            #修改字符
            self.post_mes_baidusoutu = self.post_mes_baidusoutu.replace(":","")
            return applet_public_ports.appBaidusoutu(self.post_userid, self.post_mes_baidusoutu)

        #PIC-bian-url 带管理 彼岸网
        if (eval(bot_message_app_picbian_up)):
            return applet_public_ports.appPICbianUP(self.post_userid)
        elif (eval(bot_message_app_picbian_up_no)):
            send_mes = '''你没有权力哦,只有我的周爸爸可以命令我干这种事情哦(●'◡'●)'''
            return DingDingLanguage.sendText(self.post_userid, send_mes)
        #彼岸网 主程序 分解词语
        picbian_app_panduan_ci = self.post_mes[0:self.post_mes.rfind('的')]
        if (eval(bot_message_app_picbian)):
            self.post_mes_PICbian = self.post_mes[self.post_mes.rfind('的'):]
            self.post_mes_PICbian = self.post_mes_PICbian.replace("的","")
            return applet_public_ports.appPICbian(self.post_userid,self.post_mes_PICbian)
        #彼岸网帮助
        if (self.post_mes == "彼岸网帮助"):
            return applet_public_ports.appPICbianhelp(self.post_userid)

        #随机二次元图片
        if (eval(bot_message_app_api_pixivweb)):
            return applet_public_ports.appapipixivweb(self.post_userid)

        #if (self.post_mes == '天气'):
            #send_mes = getWeather()
            #return sendMarkdown('天气预报', send_mes)

        #私人项目
        #刷小米步数 已失效
        #if (self.post_mes == "启动刷步数小程序"):
            #return siappxiaomibushu(self.post_userid)

        #xiaomi_bushu 新版小米运动刷步数
        xiaomi_bushu_init = self.post_mes[0:self.post_mes.rfind(',')]
        if (xiaomi_bushu_init == '启动刷步数小程序'):
            #内容判断
            xiaomi_bushu_bushu_init = self.post_mes[self.post_mes.rfind(':'):]
            #修改字符
            xiaomi_bushu_bushu_surr = xiaomi_bushu_bushu_init.replace(":","")
            return applet_private_ports.siappxiaomibushu2d(self.post_userid,xiaomi_bushu_bushu_surr)

        #生日项目
        if (self.post_mes == "生日功能帮助"):
            return project_private.Birtday(self.post_userid,None).Birthday_help()
        #查询指定人的生日
        Birthday_appoint_name_text = self.post_mes
        Birthday_appoint_name_fenxi = (Birthday_appoint_name_text[-3:])
        if Birthday_appoint_name_fenxi == '的生日':
            Birthday_appoint_name_fenxi_2 = (Birthday_appoint_name_text[:2])
            if Birthday_appoint_name_fenxi_2 == '查询':
                Birthday_appoint_name_end = Birthday_appoint_name_text[0:Birthday_appoint_name_text.rfind('的'):1]
                Birthday_appoint_name = (Birthday_appoint_name_end[2:])
                return project_private.Birtday(self.post_userid,Birthday_appoint_name).Birthday_appoint()

        mother_txt = self.post_mes
        mother_text_fenxi = re.sub('[^\u4e00-\u9fa5]+','',mother_txt)
        if mother_text_fenxi == "查询月生日":
            #开始分析数字
            mother_number = re.sub('[^0-9,]','',mother_txt)
            if int(mother_number) > 0 and int(mother_number) < 13:
                #开始执行查询命令
                return project_private.Birtday(self.post_userid,mother_number).Birthday_Send()

        #二级命令 查询所有的月份 如果json是空值则会报错 不修复
        elif mother_txt == '查询所有月生日':
            return project_private.Birtday(self.post_userid,None).Birthday_all_Send()

        #基层命令
        if (self.post_mes == "获得我的ID"):
            return DingDingLanguage().DicenghuodeID(self.post_userid)
        
        if (self.post_mes == "2022版私人助理介绍"):
            return DingDingLanguage.BotMesJiaoshao2022(self.post_userid)
            
        if (self.post_mes == "私人助理管理员版介绍" and self.post_isAdmin == True):
            return DingDingLanguage.BotMesJiaoshaoAdmin(self.post_userid)
        elif (self.post_mes == "私人助理管理员版介绍" and self.post_isAdmin == False):
            return DingDingLanguage.sendTextWuQuan(self.post_userid)

        #钉钉基层消息 以上判断未出现结果的 启动基层消息判断
        for uid_say, uid_id, bot_say_ku_linshi_4 in zip(self.post_mes, self.post_userid, bot_say_ku_linshi_3):
            try:
                send_mes = bot_say_ku.get(bot_say_ku_linshi_4, self.post_mes)
                return DingDingLanguage.sendText(self.post_userid, send_mes)
            except:
                pass
            
        #最后一层 如果用户的话都没有结果 那就直接复读
        else:
            return DingDingLanguage.sendText(self.post_userid, self.post_mes+'          [我是复读机(∩_∩)]')


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
    def sendTextWuQuan(post_userid):
        #只有管理员才能使用的功能,被普通用户启动的回应消息
        message = {
            "msgtype": "text",
            "text": {
                "content": "主人,你现在没有这个权限呢,不可以使用这个功能"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message

    #普通消息 长消息 钉钉自我介绍
    def BotMesJiaoshao(post_userid):
        with open(start_lu+"/bot-multiple_messages/bot-alone_mes/jieshao.json","r",encoding="utf-8") as jieshao:
            jieshao_xinxi = jieshao.read()
        jieshao_xinxi_du = eval(jieshao_xinxi)
        jieshao_xinxi_jieshao = (jieshao_xinxi_du['1'][0]["2021jieshao"])

        message = {
            "msgtype": "markdown",
            "markdown": {
                "title":"私人助理的自我介绍",
                "text": jieshao_xinxi_jieshao#上次大事件：更换服务器 2021年11月21日 21:40"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message
    def BotMesJiaoshao2022(post_userid):
        with open(start_lu+"/bot-multiple_messages/bot-alone_mes/jieshao.json","r",encoding="utf-8") as jieshao:
            jieshao_xinxi = jieshao.read()
        jieshao_xinxi_du = eval(jieshao_xinxi)
        jieshao_xinxi_jieshao = (jieshao_xinxi_du['2'][0]["2022jieshao"])

        message = {
            "msgtype": "markdown",
            "markdown": {
                "title":"私人助理的自我介绍",
                "text": jieshao_xinxi_jieshao#上次大事件：更换服务器 2021年11月21日 21:40"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message
    def BotMesJiaoshaoAdmin(post_userid):
        with open(start_lu+"/bot-multiple_messages/bot-alone_mes/jieshao.json","r",encoding="utf-8") as jieshao:
            jieshao_xinxi = jieshao.read()
        jieshao_xinxi_du = eval(jieshao_xinxi)
        jieshao_xinxi_jieshao = (jieshao_xinxi_du['admin'][0]["2022jieshaoAdmin"])

        message = {
            "msgtype": "markdown",
            "markdown": {
                "title":"私人助理的自我介绍[管理员版]",
                "text": jieshao_xinxi_jieshao#上次大事件：更换服务器 2021年11月21日 21:40"
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message

    #底层功能
    def DicenghuodeID(post_userid):
        #获取ID
        message = {
            "msgtype": "text",
            "text": {
                "content": post_userid
            },
            "at": {
                "atDingtalkIds": [post_userid],
                "isAtAll": False
            }
        }
        return message

    def sendMarkdown(title, send_mes):
        # 发送Markdown形式
        message = {
            "msgtype": "markdown",
            "markdown": {
                "title": title,
                "text": send_mes
            },
            "at": {
                "atDingtalkIds": [],
                "isAtAll": False
            }
        }
        return message

if __name__ == "__main__":
    print(DingDingLanguage("$:LWCP_v1:$lKh6TGW/6XEyY3Ho0ZAreuvmhpvC3H/R", input("输入消息：\n"), "post_userIds", None , None).selectMes())
    
