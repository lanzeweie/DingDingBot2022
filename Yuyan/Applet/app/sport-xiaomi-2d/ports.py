# -*- coding:utf-8 -*-
import sys,os
from updatabs import xiaomiyundong
start_lu = os.path.dirname(os.path.abspath(__file__))
sys.path.append(start_lu)
class xiaomiyundong_chushi():
    def user(user_ding):
        with open(f"{start_lu}/user.json","r",encoding="utf-8") as user:
            user_json = user.read()

        user_json = eval(user_json)
        user_len = len(user_json["user"])
        shu = 0
        for cishu in range(user_len):
            user = user_json["user"][shu]["userid"]
            if user == user_ding:
                phone = user_json["user"][shu]["phone"]
                password = user_json["user"][shu]["password"]
                return phone,password
            else:
                shu+=1
    def start(user_ding,step):
        user_xinxi = xiaomiyundong_chushi.user(user_ding)
        phone = user_xinxi[0]
        password = user_xinxi[1]
        xiaomiyundong_xinxi = ""
        xiaomiyundong_xinxi = xiaomiyundong.main(phone, password, step) + '\n'
        return xiaomiyundong_xinxi


if __name__ == "__main__":
    user_ding = "zhou"
    # 用户名（在数据库里的值）
    step = "1100"
    # 要修改的步数，直接输入想要修改的步数值，留空为随机步数
    (xiaomiyundong_chushi.start(user_ding,step))
