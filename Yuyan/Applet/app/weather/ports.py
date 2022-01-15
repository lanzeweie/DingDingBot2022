# -*- coding:utf-8 -*-
#weather的接口
import sys,os
start_lu = os.path.dirname(os.path.abspath(__file__))
sys.path.append(start_lu)
from weather import weather
print("成功接入 天气查询 小程序")
class weather_query():
    def query(weather_name):
        if len(sys.argv) < 2:
            city = weather_name
        else:
            city = sys.argv[1].strip()
        city_code = weather.get_location(city)
        if not city_code:
            return ('没有 '+weather_name+' 的天气情况')
        else:
            return weather.get_weather_detail(city_code)
