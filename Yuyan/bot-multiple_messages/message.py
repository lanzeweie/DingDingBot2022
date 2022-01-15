# -- coding:UTF-8 --
#快速编辑与写入
import configparser
import os

#值名：  #需要改 只支持小写
zhi = "apipixivweb"


#需要改
语句一 = '随机二次元图片'
语句二 = '随机二次元图片一张'
语句三 = '随机发送一张二次元图片'
语句四 = '随机一张二次元图片'
语句五 = '随机二次元'

xieru1 = "post_mes == " "'"+str(语句一)+"'" " or post_mes == " "'"+str(语句二)+"'" " or post_mes == " "'"+str(语句三)+"'" " or post_mes == " "'"+str(语句四)+"'" " or post_mes == " "'"+str(语句五)+"'"

#再来五条
语句六 = "发彼岸"
语句七 = "发张彼岸"
语句八 = "来张彼岸网"
语句九 = "来一张彼岸网"
语句十 = "来一张彼岸"

#需要请删除 #
#xieru2 = " or post_mes == " "'"+str(语句六)+"'" " or post_mes == " "'"+str(语句七)+"'" " or post_mes == " "'"+str(语句八)+"'" " or post_mes == " "'"+str(语句九)+"'" " or post_mes == " "'"+str(语句十)+"'"




try:
    xieru = str(xieru1+xieru2)
except:
    xieru = xieru1

rootPath = os.path.dirname(os.path.abspath(__file__))
cf = configparser.ConfigParser()
weizhi = rootPath + "/command_saemt.ini"
cf.read(weizhi,"utf-8") 
cf.set("all", zhi, xieru)

cf.write(open(weizhi, "r+", encoding="utf-8"))