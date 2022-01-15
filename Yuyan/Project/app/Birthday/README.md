# Birthday - 生日通报

## 前言
在朋友生日的时候给朋友送上一个祝福，这一定会很让ta**心头一暖吧**<br/>
正好钉钉有这个推送消息的机器人服务，能白嫖就白嫖，可以省下一大堆麻烦
> 用一点小小的祝福，温暖此刻的心

## 模块介绍
环境：Pyhon3<br/>
钉钉：企业机器人

### **主要模块**<br/>
从 json/Birthday.json 获得生日信息

#### 一.计算模块
1. main/Birthday_judge.py
    1. 主要函数  负责计算日期  内部函数名：distance(self)
        1. 传入函数格式：xxxx年xx月xx日 (可以不要xxxx年,年必须留下)
        2. 传出函数格式：('1', '19')  ------ (1) 代表剩余天数 (19) 代表年龄
    2. 内部其它可用函数
        1. __init__(self,date) [负责格式化年月字符]
            1. 传入函数格式：出生年月
            2. 传出函数格式：None
        2. judge(self) [负责判断生日是否过去|已废弃]

#### 二.查询模块
1. main/Birthday_query.py
    1. 主要函数 负责查询当前月份会过生日的人 内部函数名：Birthday_date_json(mother)
        1. 传入函数格式：只接受数字 1-12
        2. 传出函数格式：{"name": "XXX", "date": "xxxx年x月xx日"},{"name": "XXX", "date": "xxxx年x月xx日"}
    2. 内部可用函数
        1. Birthday_date_text(mother) [负责传出这个月text格式的生日信息]
            1. 传入函数格式：只接受数字 1-12
            2. 传出函数格式：text格式的信息
        2. Birthday_appoint(name) [负责传出这个人的text出生年月]
            1. 传入函数格式：姓名
            2. 传出函数格式：出生年月

#### 三.钉钉模块
1. DingDingBot.py
    1. 主要函数 输出信息
        1. 传入函数格式：DingBot(Send).DingSend()  [Send=信息]
        2. 传出函数格式：None

### **其他模块**<br/>
Query.py<br/>
调用的模块
```BirthdayQuery、BirthdayJudge```
查询这个月有哪些人要过生日，并且在 json\Birthday_news.json 写入即将过生日的人<br/>
使用格式：附带 月份[1-12] 参数启动<br/>

appoint.py<br/>
调用的模块
```BirthdayQuery```
用于接入钉钉 查询指定人的生日 [需要全字匹配]<br/>
使用格式：*查询XXX的生日*  

Birthday_DingDing_judge.py<br/>
调用的模块
```Birthday_query```
用于接入钉钉 查询生日功能 只支持查询月份 [需要全字匹配]<br/>
使用格式：*查询X月生日* *查询所有月生日*

task\Daily_task.py<br/>
调用的程序
```Query.py```
生日查询 每日启动 生日大于10天则不输出内容 如果生日小于10天则每日输出

task\Monthly_task.py<br/>
调用程序
```Birthday_query```
定时任务 每月1号执行 查询这个月有那些人过生日