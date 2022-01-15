# -*- utf-8 -*-
#接入钉钉 查询功能 只支持查询月份 不支持具体名字
#命令格式：查询X月生日
import re
import os
from main.Birthday_query import BirthdayQuery

def Birthday_DingDing_judge(mother):
    mother_txt = mother
    #判断是否符合命令格式
    mother_text_fenxi = re.sub('[^\u4e00-\u9fa5]+','',mother_txt)
    if mother_text_fenxi == "查询月生日":
        #开始分析数字
        mother_number = re.sub('[^0-9,]','',mother_txt)
        if int(mother_number) > 0 and int(mother_number) < 13:
            #开始执行查询命令
            Birthday_Send = BirthdayQuery.Birthday_date_text(mother_number)
            return Birthday_Send

    #二级命令 查询所有的月份 如果json是空值则会报错 不修复
    elif mother_txt == '查询所有月生日':
        Birthday_all_Send = ""
        for moth in range(12):
            Birthday_all_text = BirthdayQuery.Birthday_date_text(moth)
            Birthday_all_Send += Birthday_all_text
        return Birthday_all_Send 

if __name__ == "__main__":
    print(Birthday_DingDing_judge(input("输入命令格式 查询X月生日\n:")))

'''
#生日查询

    Brithday_mother_txt = post_mes
    #判断是否符合命令格式
    Brithday_mother_text_fenxi = re.sub('[^\u4e00-\u9fa5]+','',Brithday_mother_txt)
    if Brithday_mother_text_fenxi == "查询月生日":
        #开始分析数字
        Brithday_mother_number = re.sub('[^0-9,]','',Brithday_mother_txt)
        if int(Brithday_mother_number) > 0 and int(Brithday_mother_number) < 13:
            #开始执行查询命令
            Brithday_mother_number = int(Brithday_mother_number)
            return Birthday_DingDing_judge(post_userid,Brithday_mother_number)

    #二级命令 查询所有的月份 如果json是空值则会报错 不修复
    elif Birthday_mother_txt == '查询所有月生日':
        Birthday_all_Send = ""
        for Birthday_moth in range(12):
            Birthday_all_text = BirthdayQuery.Birthday_date_text(Birthday_moth)
            Birthday_all_Send += Birthday_all_text
        return Birthday_all_Send 
'''