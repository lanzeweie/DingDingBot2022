# -*- coding:utf-8 -*-
import json,os

#修改 Birthday信息库的 json数据库

class Birthday_Add():
    global intlat_json,weizhi
    weizhi = os.path.abspath(os.path.join(os.path.dirname(__file__),os.path.pardir))
    with open(weizhi+"/json/Birthday.json","r",encoding="utf-8") as f:
        intlat_by = f.read()
    intlat_json = json.loads(intlat_by)
    '''
    #获取json数据
    def intlat():
        global intlat_json
        with open(weizhi+"/json/Birthday.json","r",encoding="utf-8") as f:
            intlat_by = f.read()
        intlat_json = json.loads(intlat_by)
    '''

    #修改json数据 传参：姓名 生日 几月
    def alter(name,date,mother):
        if intlat_json["name"] == "生日信息":
            mother_inspect = [1,2,3,4,5,6,7,8,9,10,11,12]
            if mother in mother_inspect:
                #判断是否有相同姓名的人或者已经录入的人
                mother_json = "mother"+str(mother)
                alter_mother_len = len(intlat_json["list"][0][mother_json])
                for xtnamepd in range(alter_mother_len):
                    xtname_eval = eval(str([intlat_json["list"][0][mother_json][xtnamepd]]))
                    xtname = xtname_eval[0]["name"]
                    if name == xtname:
                        xtdate = xtname_eval[0]["date"]
                        if date == xtdate:
                            return "Birthday_control：数据库有此人"
                        else:
                            intlat_json["list"][0][mother_json][-1] = {'name': name, 'date': date},
                            intlat_json_write = json.dumps(intlat_json,indent=4)
                            with open(weizhi+"/json/Birthday.json","w",encoding="utf-8") as alter:
                                alter.write(intlat_json_write)
                            return f"Birthday_control：成功添加{name}至数据库"
                    else:
                        continue
                #出现不知名bug ： "" 内信息 仍被强赋值 使用笨办法 让被强赋值的值的强赋值等于值
                #笨办法依靠bug运行
                alter_json_all = str(intlat_json["list"][0][mother_json])
                alter_json_all = alter_json_all.strip().strip('[]')
                name_qiangfuzhi = "name"
                date_qiangfuzhi = "date"
                alter_json_all += ",{" + "name_qiangfuzhi" + ":'" + name + "'," + "date_qiangfuzhi" + ":'" + date + "'}"
                alter_json_all_ = eval(alter_json_all)
                intlat_json["list"][0][mother_json] = alter_json_all_
                intlat_json_write = json.dumps(intlat_json,indent=4,ensure_ascii=False)
                with open(weizhi+"/json/Birthday.json","w",encoding="utf-8") as alter:
                    alter.write(intlat_json_write)
                return f"Birthday_control：成功添加{name}至数据库"
            else:
                return f"Birthday_control：超出最大月份 {mother}"

    def alterdel(name,date,mother):
        if intlat_json["name"] == "生日信息":
            mother_inspect = [1,2,3,4,5,6,7,8,9,10,11,12]
            if mother in mother_inspect:
                mother_json = "mother"+str(mother)
                alter_mother_len = len(intlat_json["list"][0][mother_json])
                for xtnamepd in range(alter_mother_len):
                    xtname_eval = eval(str([intlat_json["list"][0][mother_json][xtnamepd]]))
                    xtname = xtname_eval[0]["name"]
                    if name == xtname:
                        xtdate = xtname_eval[0]["date"]
                        if date == xtdate:
                            del intlat_json["list"][0][mother_json][xtnamepd]
                            intlat_json_write = json.dumps(intlat_json,indent=4,ensure_ascii=False)
                            with open(weizhi+"/json/Birthday.json","w",encoding="utf-8") as alter:
                                alter.write(intlat_json_write)
                            return f"Birthday_control：成功将{name}移除数据库"
                        elif name == xtname:
                            return f"Birthday_control：数据库发现{name},但是日期信息不匹配,数据库中日期为{xtdate}"
                return f"Birthday_control：数据库未能寻找到{name}"

    def start(date):
        head_json = eval(str(date))
        name = head_json["name"]
        date = head_json["date"]
        #格式化字符
        #月
        mother = date[date.rfind('年'):]
        mother = mother.replace("年","")
        mother = mother[0:mother.rfind('月'):]
        mother = int(mother)
        return Birthday_Add.alter(name,date,mother)

    def start_del(date):
        head_json = eval(str(date))
        name = head_json["name"]
        date = head_json["date"]
        
        #格式化字符
        #月
        mother = date[date.rfind('年'):]
        mother = mother.replace("年","")
        mother = mother[0:mother.rfind('月'):]
        mother = int(mother)
        return Birthday_Add.alterdel(name,date,mother)

if __name__ == "__main__":
    #信息传入列子 {'name': '罗心喆', 'date': '2003年1月24日'}
    date = {'name': '罗心喆', 'date': '2003年3月24日'}
    print(Birthday_Add.start(date))