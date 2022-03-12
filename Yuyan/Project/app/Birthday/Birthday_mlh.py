# -*- coding:utf-8 -*-
import sys,os,json
start_lu = os.path.dirname(os.path.abspath(__file__))
sys.path.append(start_lu)
from main.Birthday_add import Birthday_Add
from main.Birthday_query import BirthdayQuery

class Birthdaymlh():
    def __init__(self,post_mes) -> str:
        self.post_mes = post_mes

    def mlh(self):
        if self.post_mes == "帮助":
            Send = "# **🎂命令级Birthday功能 帮助🎂** \n\n ## **添加用户到数据库** \n\n >@私人助手 /srml 添加用户,XXX:2000年00月00日\n\n ## **将用户移除出数据库** \n\n >@私人助手 /srml 移除用户,XXX:2000年00月00日\n\n ## **查询数据库信息** \n\n >@私人助手 /srml 查询数据库"
            return "help",Send

        if self.post_mes.find("添加用户",0,4) == 0:
            xinxi = self.post_mes[5:]
            if xinxi == "":
                return "你没有提供用户信息呢"
            name = xinxi[0:xinxi.rfind(':'):]
            date = xinxi[xinxi.rfind(':'):]
            if date[:1] != ":":
                return "命令信息不规范"
            if date[1:] == "":
                return "日期未填写"
            add_json = {"name":name,"date":date[1:]}
            return Birthday_Add.start(add_json)

        if self.post_mes.find("移除用户",0,4) == 0:
            xinxi = self.post_mes[5:]
            if xinxi == "":
                return "你没有提供用户信息呢"
            name = xinxi[0:xinxi.rfind(':'):]
            date = xinxi[xinxi.rfind(':'):]
            if date[:1] != ":":
                return "命令信息不规范"
            if date[1:] == "":
                return "日期未填写"
            add_json = {"name":name,"date":date[1:]}
            return Birthday_Add.start_del(add_json)
        
        if self.post_mes == "查询数据库" or self.post_mes == "数据库" or self.post_mes == "数据库信息" or self.post_mes == "列出数据库" or self.post_mes == "生日用户信息" or self.post_mes == "查询数据库信息":
            return BirthdayQuery.Birthday_class_mother()

        return "命令不规范,请使用 /srml 帮助 查询可用命令"

if __name__ == "__main__":
    post_mes = "日"
    print(Birthdaymlh(post_mes).mlh())