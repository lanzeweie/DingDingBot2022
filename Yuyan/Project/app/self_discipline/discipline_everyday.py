# -*- coding:utf-8 -*- 
import requests,json,os,configparser,datetime
shangji_lujin = os.path.abspath(os.path.join(os.path.dirname(__file__),"../../../.."))
start_lujin = os.path.dirname(os.path.abspath(__file__))
#每日打卡 根据zancun.ini信息的用户 进行一次全部打卡  由定时任务启动,独立程序
#如果用户在 今日 00：00-7：00 失败 ，则不计
def DingDing_single(json,accessToken):
    #配置
    url = "https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend"
    head = {
        "Host":"api.dingtalk.com",
        "x-acs-dingtalk-access-token":accessToken,
        "Content-Type":"application/json"
    }

    ione = requests.post(url,headers=head,json=json)
    print(ione.text)
    return ione.text


def DingDing_single_accessToken():
    url = "https://api.dingtalk.com/v1.0/oauth2/accessToken"
    head = {
        "Host":"api.dingtalk.com",
        "Content-Type":"application/json"
    }
    body = {
        "appKey":AppKey_set,
        "appSecret":AppSecret_set
    }
    ba =requests.post(url,headers=head,json=body)
    ba_json = json.loads(ba.text)
    ba_json_ues = (ba_json['accessToken'])
    return ba_json_ues

def DingDingSet():
    with open(f"{shangji_lujin}/data/DingDingSet.json","r",encoding="utf-8") as set:
        DingSet = set.read()
    global Webhook_set,AppSecret_set,AppKey_set
    DingSet_text = eval(DingSet)
    Webhook_set = (DingSet_text['set'][0]['Webhook'])
    AppSecret_set = (DingSet_text['set'][0]['AppSecret'])
    AppKey_set = (DingSet_text['set'][0]['AppKey'])

def main():
    #读取配置信息
    DingDingSet()
    zancun = configparser.ConfigParser()
    zancun.read(start_lujin + "/zancun.ini","utf-8")
    everyday = zancun.sections()

    accessToken = DingDing_single_accessToken()

    for uid_everyday in everyday:
        day = int(zancun.get(uid_everyday,"天数"))
        day2 = str(zancun.get(uid_everyday,"开始日"))
        day3 = datetime.datetime.now().strftime('%Y年-%m月-%d日 %H:%M')
        day += int(1)
        day1 = day
        userIds = str(zancun.get(uid_everyday,"私id"))

        try:
            loser_dangri = int(zancun.get(uid_everyday,"当日"))
            if loser_dangri == 0:
                raise
            zancun.set(uid_everyday, "当日",'0')
            zancun.write(open(start_lujin + "/zancun.ini", "r+", encoding="utf-8"))
            DingDing_single_xiaoxiti_json = {
            "robotCode" : AppKey_set,
            "userIds" : [ userIds ],
            "msgKey" : "sampleText",
            "msgParam" : {"content": "👼健康生活👼 \n今日不计" }
            }
            DingDing_single(DingDing_single_xiaoxiti_json,accessToken)
        except:
            zancun.set(uid_everyday, "天数",str(+day1))
            zuigaoday = int(zancun.get(uid_everyday,"最高"))
            if day1 > zuigaoday:
                zancun.set(uid_everyday, "最高",str(+day1))
            zancun.write(open(start_lujin + "/zancun.ini", "r+", encoding="utf-8"))
            Send = "👼健康生活👼 \n 恭喜你又又坚持了一天！！！\n 可喜可贺~可喜可贺 (∩_∩)  \n 新的一天也要坚持下去哦！\n 加油加油(ง •_•)ง  \n-------------------\n " +str(day2)+" \n -----至----- \n "+str(day3)+" \n 至今你已经坚持了："+str(day1)+" 天 \n 请务必保持下去哦 o(*￣▽￣*)o"
            DingDing_single_xiaoxiti_msgParam_bianliang = ({"content":Send})
            DingDing_single_xiaoxiti_json = {
            "robotCode" : AppKey_set,
            "userIds" : [ userIds ],
            "msgKey" : "sampleText",
            "msgParam" : ''+str(DingDing_single_xiaoxiti_msgParam_bianliang)+''
            }
            DingDing_single(DingDing_single_xiaoxiti_json,accessToken)
    
main()
