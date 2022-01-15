# -- coding:UTF-8 --
#快速编辑与写入  只接收指定人的消息
import configparser
import os

#值名：  #需要改 只支持小写
zhi = "app-PICbian_UP"
#指定人 需要 post_userid 一般用作为管理员
uid = "$:LWCP_v1:$lKh6TGW/6XEyY3Ho0ZAreuvmhpvC3H/R"

#需要改
语句一 = '更新彼岸网的图片'
语句二 = '更新彼岸的图片'
语句三 = '更新彼岸'
语句四 = '管理员命令：更新所有爬虫'
语句五 = '更新彼岸网'

xieru = "post_mes == " "'"+str(语句一)+"'"" and post_userid == ""'"+str(uid)+"'" " or post_mes == " "'"+str(语句二)+"'"" and post_userid == ""'"+str(uid)+"'" " or post_mes == " "'"+str(语句三)+"'"" and post_userid == ""'"+str(uid)+"'" " or post_mes == " "'"+str(语句四)+"'"" and post_userid == ""'"+str(uid)+"'" " or post_mes == " "'"+str(语句五)+"'"" and post_userid == ""'"+str(uid)+"'"

#对应非管理员的人消息
xieru_no = "post_mes == " "'"+str(语句一)+"'" " or post_mes == " "'"+str(语句二)+"'" " or post_mes == " "'"+str(语句三)+"'" " or post_mes == " "'"+str(语句四)+"'" " or post_mes == " "'"+str(语句五)+"'"

rootPath = os.path.dirname(os.path.abspath(__file__))
cf = configparser.ConfigParser()
weizhi = rootPath + "/command_saemt.ini"
print(weizhi)
cf.read(weizhi,"utf-8") 
cf.set("all", zhi, xieru)
cf.set("all", zhi+"_no", xieru_no)

cf.write(open(weizhi, "r+", encoding="utf-8"))