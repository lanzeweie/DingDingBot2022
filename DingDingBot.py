# -- coding:UTF-8 --
from multiprocessing import Process
import json,time,hmac,hashlib,base64,socket,requests,os,zipfile,datetime
from Mokai.Data_life import TTLDict
from Yuyan.DingBot_language import DingDingLanguage
DingDing_single_shujuhuancunTime = TTLDict()

def DingDing_client(self,Token):
    global accessToken
    accessToken = Token
    # 获取socket
    request_data = client_socket.recv(20000)
    post_userid, post_sign, post_timestamp, post_mes, post_moshi, post_userids, post_isAdmin, post_senderNick = DingDing_chushihua(request_data)
    print(f"\n用户消息：{post_mes}")
    print(f"聊天模式：{post_moshi} ",end="")
    print(f"用户名称：{post_senderNick}\n",end="")
    print(f"用户群ID：{post_userid} ",end="")
    print(f"用户私ID：{post_userids}")
    now_log_detime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    log_mess = {(f"用户消息：{post_mes}"),(f"聊天模式：{post_moshi} "),(f"用户名称：{post_senderNick}"),(f"用户群ID：{post_userid} "),(f"用户私ID：{post_userids}")}
    #日志录入
    with open((now_weizhi+"/log/last.log"),"a",encoding="utf-8") as last_log:
        last_log.write("\n"+(now_log_detime)+"\n用户发送消息："+str(log_mess)+"\n")
    # 使用socket 回应钉钉 并查看模式
    if post_moshi == "2":
        #群聊模式
        DingDing_group(post_userid, post_sign, post_timestamp, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi)
    if post_moshi == "1":
        #单聊模式
        DingDing_single(post_userid, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi)
    # 关闭socket
    client_socket.close()

def DingDing_chushihua(request_data):
    #从DingDing_client 收到用户发到钉钉 钉钉发到程序的json包,解析它
    request_data = str(request_data, encoding="utf-8").split('\r\n')
    items = []
    for item in request_data[1:-2]:
        items.append(item.split(':'))
    dd_post_useful = {}
    for i in items:
        dd_post_useful.update({i[0]: i[1]})
    if dd_post_useful.get('sign') == None:
        print('other connect')
        return 0
    else:
        post_sign = dd_post_useful.get('sign').strip()
        post_timestamp = dd_post_useful.get('timestamp').strip()
        
        #主要参数 可自行增加
        dd_post_xinxiti = json.loads(request_data[-1])
        post_userid = dd_post_xinxiti.get('senderId').strip()
        post_mes = dd_post_xinxiti.get('text').get('content').strip()
        post_moshi = dd_post_xinxiti.get('conversationType').strip()
        post_userids = dd_post_xinxiti.get('senderStaffId').strip()
        post_isAdmin = dd_post_xinxiti.get('isAdmin')
        post_senderNick = dd_post_xinxiti.get('senderNick')

    return post_userid, post_sign, post_timestamp, post_mes, post_moshi, post_userids, post_isAdmin, post_senderNick

def DingDingSet():
    lujin = os.path.dirname(os.path.abspath(__file__))
    with open(f"{lujin}/data/DingDingSet.json","r",encoding="utf-8") as set:
        DingSet = set.read()
    global Webhook_set,AppSecret_set,AppKey_set,Post_set
    DingSet_text = eval(DingSet)
    Webhook_set = (DingSet_text['set'][0]['Webhook'])
    AppSecret_set = (DingSet_text['set'][0]['AppSecret'])
    AppKey_set = (DingSet_text['set'][0]['AppKey'])
    Post_set = (DingSet_text['set'][0]['Post'])

def DingDing_group(post_userid, post_sign, post_timestamp, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi):
    # 配置token
    # 得到当前时间戳
    timestamp = str(round(time.time() * 1000))
    # 计算签名
    app_secret = AppSecret_set
    app_secret_enc = app_secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(post_timestamp, app_secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(app_secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = base64.b64encode(hmac_code).decode('utf-8')
    # 验证是否来自钉钉的合法请求
    if (abs(int(post_timestamp) - int(timestamp)) < 3600000 and post_sign == sign):
        webhook=Webhook_set
        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
        # 发送消息
        message_json = json.dumps(DingDingLanguage(post_userid, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi).selectMes())
        #日志录入
        now_log_detime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
        with open((now_weizhi+"/log/last.log"),"a",encoding="utf-8") as last_log:
            last_log.write((now_log_detime)+"\n"+f"群聊投出消息：{message_json}"+"\n")
        # 返回发送状态
        info = requests.post(url=webhook, data=message_json, headers=header)
        print(info.text)
    else:
        print("Warning:Not DingDing's post")

def DingDing_single(post_userid, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi):
    #与群聊获得消息的接口一致，获取后转义成可识别语句
    url = "https://api.dingtalk.com/v1.0/robot/oToMessages/batchSend"
    head = {
        "Host":"api.dingtalk.com",
        "x-acs-dingtalk-access-token":accessToken,
        "Content-Type":"application/json"
    }

    DingDing_single_message_json = json.dumps(DingDingLanguage(post_userid, post_mes, post_userids, post_senderNick, post_isAdmin, post_moshi).selectMes())
    DingDing_single_message_json_xiaoxiti = (DingDing_single_message_json)
    DingDing_single_message_json_zhuanyi = (DingDing_single_xiaoxiti_zhuanyi(post_userids, DingDing_single_message_json_xiaoxiti))
    print(f"投出消息\n{DingDing_single_message_json_zhuanyi}")
    #日志录入
    now_log_detime = datetime.datetime.now().strftime('[%Y-%m-%d %H:%M:%S]')
    with open((now_weizhi+"/log/last.log"),"a",encoding="utf-8") as last_log:
        last_log.write((now_log_detime)+"\n"+f"私聊投出消息：{DingDing_single_message_json_zhuanyi}"+"\n")
    info = requests.post(url,headers=head,json=DingDing_single_message_json_zhuanyi)
    info_text = eval(info.text)
    if info.text["message"] == "不合法的access_token":
        print("access_token过期，已经重新获取并且重新发送消息")
        time.sleep(0.2)
        info = requests.post(url,headers=head,json=DingDing_single_message_json_zhuanyi)
        info_text = eval(info.text)
    try:
        single_message_text = info_text["message"]
        if single_message_text == "msgParam必须是json格式":
            single_message_chongshi = json.dumps(DingDingLanguage.send_single_error(post_userid))
            DingDing_single_message_json_xiaoxiti = (single_message_chongshi)
            DingDing_single_message_json_zhuanyi = (DingDing_single_xiaoxiti_zhuanyi(post_userids, DingDing_single_message_json_xiaoxiti))
            info = requests.post(url,headers=head,json=DingDing_single_message_json_zhuanyi)
            print(f"获得回应\n{info.text}")
    except:
        print(f"获得回应\n{info.text}")

def DingDing_single_xiaoxiti_zhuanyi(post_userids, send_mes):
    send_mes = json.loads(send_mes)
    DingDing_single_xiaoxiti_moshi = send_mes['msgtype']
    if DingDing_single_xiaoxiti_moshi == "text":
        DingDing_single_xiaoxiti_msgKey = "sampleText"
        DingDing_single_xiaoxiti_msgParam = send_mes['text']['content']

        DingDing_single_xiaoxiti_msgParam_bianliang = ({"content":DingDing_single_xiaoxiti_msgParam})
        DingDing_single_xiaoxiti_json = {
        "robotCode" : AppKey_set,
        "userIds" : [ post_userids ],
        "msgKey" : DingDing_single_xiaoxiti_msgKey,
        "msgParam" : ''+str(DingDing_single_xiaoxiti_msgParam_bianliang)+''
        }
        return DingDing_single_xiaoxiti_json
    if DingDing_single_xiaoxiti_moshi == "markdown":
        DingDing_single_xiaoxiti_msgKey = "sampleMarkdown"
        DingDing_single_xiaoxiti_msgParam_title = send_mes['markdown']['title']
        DingDing_single_xiaoxiti_msgParam_text = send_mes['markdown']['text']

        DingDing_single_xiaoxiti_msgParam_bianliang = ({"text": DingDing_single_xiaoxiti_msgParam_text,"title": DingDing_single_xiaoxiti_msgParam_title})
        DingDing_single_xiaoxiti_json = {
        "robotCode" : AppKey_set,
        "userIds" : [ post_userids ],
        "msgKey" : DingDing_single_xiaoxiti_msgKey,
        "msgParam" : ''+str(DingDing_single_xiaoxiti_msgParam_bianliang)+''
        }
        return DingDing_single_xiaoxiti_json

def DingDing_single_accessToken_chushihua():
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

def DingDing_single_accessToken_yanzheng_backup():
    DingDing_single_accessToken_up = (DingDing_single_shujuhuancunTime['accessToken'])
    if DingDing_single_accessToken_up == DingDing_single_accessToken_time_Token_chushi:
        return DingDing_single_accessToken_up

def DingDing_single_accessToken_time():
    DingDing_single_shujuhuancunTime.setex('accessToken', 7200, DingDing_single_accessToken_chushihua())
    global DingDing_single_accessToken_time_Token_chushi
    DingDing_single_accessToken_time_Token_chushi = (DingDing_single_shujuhuancunTime['accessToken'])

def DingDing_single_accessToken_yanzheng():
    try:
        DingDing_single_accessToken = (DingDing_single_shujuhuancunTime['accessToken'])
    except:
        DingDing_single_accessToken = "errow"
    if DingDing_single_accessToken == DingDing_single_accessToken_time_Token_chushi:
        return DingDing_single_accessToken
    else:
        print("\n身份码过期,重新获取")
        DingDing_single_accessToken_time()
        DingDing_single_accessToken_backup = DingDing_single_accessToken_yanzheng_backup()
        return DingDing_single_accessToken_backup

if __name__ == "__main__":
    DingDingSet()
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server_socket.bind(("", Post_set))
        print("钉钉机器人启动成功")
    except:
        print("启动失败 端口被占用")
        print("\n👇报错信息")
        raise
    server_socket.listen(120)

    DingDing_single_accessToken_time()

    #保存日志，如果日志存在则压缩先前日志
    now_weizhi = os.path.dirname(os.path.abspath(__file__))
    log_path = os.path.join(now_weizhi, 'log')
    if not os.path.exists(log_path):
        os.mkdir(log_path)
    last_log_file = os.path.join(log_path, 'last.log')
    if os.path.exists(last_log_file):
        date_str = time.strftime('%Y-%m-%dI%H-%M-%S', time.localtime())
        new_log_file = os.path.join(log_path, f'{date_str}_last.log')
        os.rename(last_log_file, new_log_file)
    with open(last_log_file, 'w') as f:
        pass
    # 压缩上一次的日志文件
    try:
        if os.path.exists(new_log_file):
            with zipfile.ZipFile(f'{new_log_file}.zip', 'w') as z:
                z.write(new_log_file, os.path.basename(new_log_file))
            os.remove(new_log_file)
    except:
        pass
    
    while True:
        accessToken = DingDing_single_accessToken_yanzheng()
        client_socket, client_address = server_socket.accept()
        
        handle_client_process = Process(target=DingDing_client, args=(client_socket,accessToken,))
        handle_client_process.start()
        client_socket.close()
