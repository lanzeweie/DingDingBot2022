# 钉钉企业机器人2022版
下载模块： ``multiprocessing,requests,json,time,hmac,hashlib,base64,socket,os``<br/>
本地模块：[时效变量](./Mokai/Data_life.py)

## 使用
前景：已经从钉钉官网配置好了**钉钉企业机器人**并加进了钉钉群<br/>
填写钉钉企业机器人的参数 [配置文件](./data/DingDingSet.json)<br/>

启动：<br/>
```python3 DingDingBot.py```

>注意此程序无法被钉钉Ping到,所以无法被官网验证,就无法编辑机器人信息。<br/>
>因此要在官网编辑机器人信息需要单独启动验证文件<br/>
>验证程序启动：```python3 Yan.py ```<br/>

浏览器访问： ```公网IP:端口``` 查询验证程序是否启动,如果无法访问,请检查公网是否能访问,防火墙端口是否打开<br/>
*注：只有需要在官网编辑机器人信息才需要启动验证程序*

## 运行简介：
使用 socket 搭建服务端 接受来自钉钉的消息 
每收到一个消息,则单独启动一个线程进行消息判断<br/>
[运行结构介绍图](./README/4.png)  

## 主程序介绍
1. DingDingBot.py<br/>
[主程序内部函数参数介绍](./README/DingDingBot.md)  
***

### 传参介绍
DingDing_group传出的参数有
```dd_post_userid, dd_post_sign, dd_post_timestamp, dd_post_mes, dd_post_userIds, dd_post_senderNick, dd_post_isAdmin```

DingDing_single传出的参数有
```dd_post_userid, dd_post_mes, dd_post_userIds, dd_post_senderNick, dd_post_isAdmin```

### 模块介绍
- [语言模块](./Yuyan/README.md)

### 文件结构
![文件结构无注释版](./README/1.png)   
![文件结构注释版](./README/2.png)   
![文件结构详解版](./README/3.png)  
