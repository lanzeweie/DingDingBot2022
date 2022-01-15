from crontab import CronTab
import configparser
import os

rootPath = os.path.dirname(os.path.abspath(__file__))
# 创建当前用户的crontab，当然也可以创建其他用户的，但得有足够权限
my_user_cron = CronTab(user=True)
# 创建任务
job = my_user_cron.new(command='/usr/bin/python3 '+rootPath+'/start1-every_day.py 2> /dev/null > /dev/null')
# 设置任务执行周期，每两分钟执行一次
job.setall('30 7 * * *')
# 同时可以给任务设置comment，这样就可以根据comment查询，很方便

job.set_comment("钉钉戒撸打卡每日定时任务")
 
# 根据comment查询，当时返回值是一个生成器对象，不能直接根据返回值判断任务是否#存在，如果只是判断任务是否存在，可直接遍历my_user_cron.crons
 
iter = my_user_cron.find_comment('钉钉任务')
# 任务的disable和enable， 默认enable
 
job.enable(False)
 
job.enable()
print("定时任务已成功载入")
# 最后将crontab写入配置文件
 
my_user_cron.write() 

#操作指南
#输入：
#crontab -e
#写入：
#30 7 * * * /usr/bin/python3 /sirenkongjian/python-gongcheng/dingdingbot/jiankang/start1.py
#保存
#健康生活