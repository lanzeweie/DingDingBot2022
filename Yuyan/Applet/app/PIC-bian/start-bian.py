# -- coding: UTF-8 --
import os
from concurrent.futures import ThreadPoolExecutor
import time
import json
import datetime

starttime = datetime.datetime.now()
#更新程序 一次性并行运行
#1风景\n2. 2美女\n3. 3游戏\n4. 4动漫\n5. 5影视\n6. 6明星\n7. 7汽车\n8. 8动物\n9. 9人物\n10. 10美食\n11. 11宗教\n12. 12背景\n")

weizhi = os.path.dirname(os.path.abspath(__file__))

rizhiweizhi = (weizhi+"/up.log")
ok = 0

def load_and_1():
    os.system("python3 "+weizhi+"/bian-url.py 1")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_2():
    os.system("python3 "+weizhi+"/bian-url.py 2")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_3():
    os.system("python3 "+weizhi+"/bian-url.py 3")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_4():
    os.system("python3 "+weizhi+"/bian-url.py 4")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_5():
    os.system("python3 "+weizhi+"/bian-url.py 5")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_6():
    os.system("python3 "+weizhi+"/bian-url.py 6")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_7():
    os.system("python3 "+weizhi+"/bian-url.py 7")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_8():
    os.system("python3 "+weizhi+"/bian-url.py 8")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_9():
    os.system("python3 "+weizhi+"/bian-url.py 9")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_10():
    os.system("python3 "+weizhi+"/bian-url.py 10")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_11():
    os.system("python3 "+weizhi+"/bian-url.py 11")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)
def load_and_12():
    os.system("python3 "+weizhi+"/bian-url.py 12")
    global ok
    ok += 1
    if (ok == 12):
        return GGGGGG(ok)

pool=ThreadPoolExecutor(5)

a=pool.submit(load_and_1)
a=pool.submit(load_and_2)
a=pool.submit(load_and_3)
a=pool.submit(load_and_4)
a=pool.submit(load_and_5)
a=pool.submit(load_and_6)
a=pool.submit(load_and_7)
a=pool.submit(load_and_8)
a=pool.submit(load_and_9)
a=pool.submit(load_and_10)
a=pool.submit(load_and_11)
a=pool.submit(load_and_12)


rizhi_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
rizhi = ("收到启动更新程序命令时间："+rizhi_now+"\n")
with open(rizhiweizhi, "a+", encoding='utf-8') as f:
    f.write(str(rizhi))

def GGGGGG(ok):
    if (ok == 12):
        #输出钉钉
        url_hang = -1
        for url_hang, line in enumerate(open(weizhi+"/img/4kbeijing.txt", 'r', encoding='UTF-8')):
            pass
        url_hang += 1

        url_hang1 = -1
        for url_hang1, line in enumerate(open(weizhi+"/img/4kdongman.txt", 'r', encoding='UTF-8')):
            pass
        url_hang1 += 1
        
        url_hang2 = -1
        for url_hang2, line in enumerate(open(weizhi+"/img/4kdongwu.txt", 'r', encoding='UTF-8')):
            pass
        url_hang2 += 1

        url_hang3 = -1
        for url_hang3, line in enumerate(open(weizhi+"/img/4kfengjing.txt", 'r', encoding='UTF-8')):
            pass
        url_hang3 += 1

        url_hang4 = -1
        for url_hang4, line in enumerate(open(weizhi+"/img/4kmeinv.txt", 'r', encoding='UTF-8')):
            pass
        url_hang4 += 1

        url_hang5 = -1
        for url_hang5, line in enumerate(open(weizhi+"/img/4kmeishi.txt", 'r', encoding='UTF-8')):
            pass
        url_hang5 += 1

        url_hang6 = -1
        for url_hang6, line in enumerate(open(weizhi+"/img/4kmingxing.txt", 'r', encoding='UTF-8')):
            pass
        url_hang6 += 1

        url_hang7 = -1
        for url_hang7, line in enumerate(open(weizhi+"/img/4kqiche.txt", 'r', encoding='UTF-8')):
            pass
        url_hang7 += 1

        url_hang8 = -1
        for url_hang8, line in enumerate(open(weizhi+"/img/4krenwu.txt", 'r', encoding='UTF-8')):
            pass
        url_hang8 += 1

        url_hang9 = -1
        for url_hang9, line in enumerate(open(weizhi+"/img/4kyingshi.txt", 'r', encoding='UTF-8')):
            pass
        url_hang9 += 1

        url_hang10 = -1
        for url_hang10, line in enumerate(open(weizhi+"/img/4kyouxi.txt", 'r', encoding='UTF-8')):
            pass
        url_hang10 += 1

        url_hang11 = -1
        for url_hang11, line in enumerate(open(weizhi+"/img/4kzongjiao.txt", 'r', encoding='UTF-8')):
            pass
        url_hang11 += 1



        urlh = '主人久等啦\n已经成功更新彼岸网！！\n更新内容：\n'
        try:
            urlh += '背景图：'+str(url_hang)+' 张\n'
            urlh += '动漫图：'+str(url_hang1)+' 张\n'
            urlh += '动物图：'+str(url_hang2)+' 张\n'
            urlh += '风景图：'+str(url_hang3)+' 张\n'
            urlh += '妹子图：'+str(url_hang4)+' 张\n'
            urlh += '美食图：'+str(url_hang5)+' 张\n'
            urlh += '明星图：'+str(url_hang6)+' 张\n'
            urlh += '跑车图：'+str(url_hang7)+' 张\n'
            urlh += '人物图：'+str(url_hang8)+' 张\n'
            urlh += '电影图：'+str(url_hang9)+' 张\n'
            urlh += '游戏图：'+str(url_hang10)+' 张\n'
            urlh += '宗教图：'+str(url_hang11)+' 张\n'
        except:
            pass


        urlhhs = 0 
        urlhhs += int(url_hang) + int(url_hang1) + int(url_hang2) + int(url_hang3) + int(url_hang4) + int(url_hang5) + int(url_hang6) + int(url_hang7) + int(url_hang8) + int(url_hang9) + int(url_hang10) + int(url_hang11)
        endtime = datetime.datetime.now()

        print(str(urlh)+"此次一共更新了："+str(urlhhs)+" 张图片！！\n可喜可贺 ~ 可喜可贺\nO(∩_∩)O \n此次更新花费："+str(endtime - starttime)+" 秒")
