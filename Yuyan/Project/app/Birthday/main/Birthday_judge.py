# -*- coding: utf-8 -*-
import datetime
import time
#主要的函数 负责计算日期

class BirthdayJudge():
    def __init__(self,date) -> int:
        #格式化字符 提取关键信息 并全局使用
        #年
        year = date[0:date.rfind('年'):]
        self.year = year
        #月
        mother = date[date.rfind('年'):]
        mother = mother.replace("年","")
        mother = mother[0:mother.rfind('月'):]
        self.mother = mother
        #日
        day = date[date.rfind('月'):]
        day = day.replace("月","")
        day = day.replace("日","")
        self.day = day
        #现在的日期
        now_year = datetime.datetime.now().strftime("%Y")
        self.now_year = now_year
        now_mother = datetime.datetime.now().strftime("%m")
        self.now_mother = now_mother
        now_day = datetime.datetime.now().strftime("%d")
        self.now_day = now_day
    
    def judge(self):
        #比较大小 判断生日是否已经过去
        if self.mother > self.now_mother:
            print('还没过生呢')
        elif self.mother == self.now_mother:
            if self.day < self.now_day:
                print('生日已经过去')
            elif self.day == self.now_day:
                print('今天是生日')
            else:
                print('还没过生呢')
        elif self.mother < self.now_mother:
            print('生日已经过去了')

    def distance(self):
        #计算日期差
        date = f"{self.now_year}-{self.mother}-{self.day}"
        date = str(date)
        #把str的日期转换成可计算日期
        date_datetime = datetime.datetime.strptime(date, "%Y-%m-%d")
        date_now = f"{self.now_year}-{self.now_mother}-{self.now_day}"
        date_now_datetime = datetime.datetime.strptime(date_now, "%Y-%m-%d")
        date_diff = date_datetime - date_now_datetime
        date_diff = str(date_diff)
        #只保留数字 将负数转为正数 
        date_cha = date_diff[0:date_diff.rfind('d'):]
        if date_cha == '0:00:0':
            date_cha = str(0)
        #不可以转换成负数 此方案抛弃
        #date_day = date_cha.replace("-","")
        date_day = date_cha
        #计算年龄 要判断有没有给出年龄这个值 如果没有给出年龄 为了防止程序报错 把年龄定到9999岁开始减少
        date_year_len = len(self.year)
        if date_year_len == 0:
            date_year = 9999
        else:
            date_year = int(self.now_year) - int(self.year)
        return (f"{int(date_day)}"),(f"{int(date_year)}")

if __name__ == "__main__":
    BirthdayJudge("2003年11月26日").judge()
    BirthdayJudge("2003年3月26日").distance()