# -- coding:UTF-8 --
#钉钉基层消息快速编辑与写入
import configparser
import os


#类别：  必须填写   分类
print("快捷编辑系统")
lei = input('消息类别：')
#用户说的话
say = input('用户说的话：')
#机器人回复的话
say_bot = input('机器人回复的话：')

#只支持 一对一 单写





bot_me_w = os.path.dirname(os.path.abspath(__file__))
bot_me = configparser.ConfigParser()

bot_me.read(bot_me_w + "/bot_message.ini","utf-8")



def bot_mes():
    try:
        bot_me.options(lei)
        bot_me.set(lei, say, say_bot)
    except:
        bot_me.add_section(lei)
        bot_mes()

bot_mes()

bot_me.write(open(bot_me_w + "/bot_message.ini", "w+", encoding="utf-8"))



