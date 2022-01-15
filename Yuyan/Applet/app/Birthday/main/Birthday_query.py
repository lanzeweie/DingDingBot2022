# -*- coding:utf-8 -*-
import json
import os
import re
#主要的函数 负责查询日期
weizhi = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))

class BirthdayQuery():
    
    def __init__(self) -> None:
        pass

    def Birthday_date_json(mother):
        #传参查询当前月份的人 只接受数字 1-12  输出结果为json模式
        B_date_mother = int(mother)
        with open(weizhi+"/json/Birthday.json","r",encoding="utf-8") as f:
            B_date_text = f.read()
        B_date_json = json.loads(B_date_text)
        B_date_mother_id = ['mother1','mother2','mother3','mother4','mother5','mother6','mother7','mother8','mother9','mother10','mother11','mother12']
        B_date_mother_end = B_date_mother - 1
        B_date_mother_name = B_date_mother_id[B_date_mother_end]
        B_date_mother_len = len(B_date_json['list'][0][B_date_mother_name])
        B_date_json_list = ""
        for shu in range(B_date_mother_len):
            B_date_json_list = B_date_json_list + f"{str(B_date_json['list'][0][B_date_mother_name][shu])},"
        B_date_json_list = B_date_json_list[:-1]
        B_date_json_list = B_date_json_list.replace("'",'"')
        return B_date_json_list

    def Birthday_date_text(mother):
        #将json转换为具体信息
        B_date_text = BirthdayQuery.Birthday_date_json(mother)
        B_date_text_list = eval(B_date_text)
        B_date_text_list_len = (len(B_date_text_list))
        B_date_txt = ""
        #如果json文本 只有一个用户的信息 则会无法输出，但是再加一个列 ,{"name":"End"} 就可以避开这个问题
        #使用 try + except 只要出现问题则跳转到第二个添加列的补救措施上
        try:
            for shu in range(B_date_text_list_len):
                name = (B_date_text_list[shu]['name'])
                date = (B_date_text_list[shu]['date'])
                B_date_txt += (f'姓名:{name},生日:{date}\n')
        except:
            B_date_text_list_2 = B_date_text + (',{"name":"End"}')
            B_date_text_list_2 = eval(B_date_text_list_2)
            B_date_text_list_len_2 = (len(B_date_text_list_2))
            B_date_txt_2 = ''
            for shu_2 in range(B_date_text_list_len_2):
                name = (B_date_text_list_2[shu_2]['name'])
                if name == 'End':
                    continue
                date = (B_date_text_list_2[shu_2]['date'])
                B_date_txt_2 += (f'姓名:{name},生日:{date}\n')
                return B_date_txt_2
        return B_date_txt
    
    def Birthday_appoint(name):
        #查询指定人的生日
        with open(weizhi+'/json/Birthday.json','r',encoding='utf-8') as xinxi:
            Birthday_text = xinxi.read()

        #开始寻找这个名字 从头开始找
        Birthday_json = json.loads(Birthday_text)
        Birthday_json_list_moth = Birthday_json['list'][0]
        Birthday_json_list_moth_len = len(Birthday_json_list_moth)
        #print(Birthday_json_list_moth_len)

        for shu in range(Birthday_json_list_moth_len):
            Birthday_json_moth = Birthday_json_list_moth[f'mother{shu+1}']
            Birthday_json_moth_len = len(Birthday_json_moth)
            #print(Birthday_json_moth_len)
            for shu_2 in range(Birthday_json_moth_len):
                Birthday_json_moth_name = Birthday_json_moth[shu_2]['name']
                if Birthday_json_moth_name == name:
                    Birthday_json_moth_date = Birthday_json_moth[shu_2]['date']
                    return Birthday_json_moth_date
                else:
                    pass
    
        

if __name__ == "__main__":
    #print(BirthdayQuery.Birthday_date_json(input("输入月份 纯数字\n:")))
    #print(BirthdayQuery.Birthday_date_text(input("输入月份 纯数字\n:")))
    print(BirthdayQuery.Birthday_appoint(input("输入名字 \n:")))
