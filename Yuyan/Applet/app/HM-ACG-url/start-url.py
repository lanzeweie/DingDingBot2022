import requests
from lxml import html
import os
from multiprocessing.dummy import Pool
import time
import json

#魔改 https://blog.csdn.net/qq_45753992/article/details/113813352 的爬虫   结果：将爬到的 url值 写入txt 好以钉钉机器人图片发送对接

#下载图片的函数，使用多线程下载
#def down_img(arr):
    #headers = {
    #    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    #}
    #content = requests.get(url=arr[1][0], headers=headers).content
    #with open(arr[0], 'wb')as fp:
    #    fp.write(content)
    #print("下载完成一张")
    #time.sleep(0.3)

#处理图片文件夹的标题
#def correct_title(title):
    #error_set = ['/', '\\', ':', '*', '?', '"', '|', '<', '>']
    #for c in title:
        #if c  in error_set:
            #title = title.replace(c, '')
    #return title

#得到当前文件地址
urlweizhi = os.path.dirname(os.path.abspath(__file__))
zuheweizhi = urlweizhi+"/url.txt"
print("已经收到管理员命令:更新幻猫ACG图片")
dayzuheweizhi = urlweizhi+"/url.log"

if __name__=="__main__":
    start = time.time()
    etree = html.etree

    #ajax请求的url
    url = 'https://www.hmecy.com/wp-admin/admin-ajax.php?action=zrz_load_more_posts'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    #所有图片的url链接储存在这里
    all_url = []
    #if not os.path.exists('./erciyuan'):
        #os.mkdir('./erciyuan')

    #下载前4页的图片，可以根据自己需要更改循环次数
    for num in range(1,6):
        data = {
            'type': 'tag42',
            'paged': str(num)
        }
        #获取请求到的json函数
        response = requests.post(url=url,headers=headers,data=data).json()
        #分析json函数，发现html代码在key为msg的value中
        response = str(response['msg'])

        tree = etree.HTML(response)
        data_list = tree.xpath('//a[@class="link-block"]/@href')
        for urls in data_list:
            page_text = requests.get(url=urls,headers=headers).text
            detail_tree = etree.HTML(page_text)
            #获取标题
            #title = detail_tree.xpath('//*[@id="post-single"]/h1/text()')
            #修改标题
            #titles = correct_title(str(title))
            #存储的文件夹路径
            #paths = './erciyuan/' + str(titles)
            url_list = detail_tree.xpath('//*[@id="content-innerText"]//img')
            data_ins = []
            i = 0
            #创建文件夹
            #if not os.path.exists(paths):
                #os.mkdir(paths)
            for ins in url_list:
                #获取图片的url
                data_url = ins.xpath('./@src')
                #图片的存储路径
                #path = paths +'/'+ str(i) +'.jpg'
                i=i+1
                #将路径与图片的url存储到all_url中，方便后面使用多线程下载
                #all_url.append([path,data_url])
                
                #存储
                with open(zuheweizhi,"a+") as f:
                    f.write(str(data_url)+"\n")
        #去除重复行 使用系统命令 然后返回值 写入文本
        cmd = os.popen('sort '+zuheweizhi+' |uniq').read()
      
        with open(zuheweizhi,"w+") as f:
            f.write(str(cmd))  

        
        #json 储存日志
        timeday_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        try:
            with open(dayzuheweizhi,encoding='utf-8') as f:
                timeday_last = json.load(f)
            timeday = [timeday_now+" 更新成功",timeday_last]
            with open(dayzuheweizhi, "w+", encoding='utf-8') as outfile:
                json.dump(str(timeday), outfile,ensure_ascii=False,indent=1)
        except:
            with open(dayzuheweizhi, "w+", encoding='utf-8') as outfile:
                json.dump(str(timeday_now+" 更新成功"), outfile,ensure_ascii=False,indent=4)




    #创建4个线程
    #pool = Pool(4)
    #将函数与all_url列表放入线程
    #pool.map(down_img,all_url)
    #print(time.time()-start)