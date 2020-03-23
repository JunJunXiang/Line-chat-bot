########## get_weather
## Argument:經度、緯度
## Return:String 直接給chatbot回應
## 使用Openweathermap API

import requests
import json

def k_to_c(k):
    return k - 273.15

def get_weather(lat, lon):
    ret_data = ''
    appid = '800a7ab29709951ce4868c459dd741c8'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    data = {
        'lat':str(lat),
        'lon':str(lon),
        'appid':appid
    }
    try:
        res = requests.get(url,params=data)
        jdata = json.loads(res.text)
        dict_data = {
            '經度': str(jdata['coord']['lon']),
            '緯度': str(jdata['coord']['lat']),
            '城市': str(jdata['name']),
            '天氣': str(jdata['weather'][0]['main']),
            '現在溫度': str(k_to_c(jdata['main']['temp']))[:5],
            '最高溫度': str(k_to_c(jdata['main']['temp_max']))[:5],
            '最低溫度': str(k_to_c(jdata['main']['temp_min']))[:5],
        }
        ret_data = '經度： ' + dict_data['經度'] +\
              '\n緯度： ' + dict_data['緯度'] +\
              '\n城市： ' + dict_data['城市'] +\
              '\n天氣：' + dict_data['天氣'] +\
              '\n現在溫度： ' + dict_data['現在溫度'] + \
              '\n最高溫度： ' + dict_data['最高溫度'] + '\n最低溫度： ' + dict_data['最低溫度']

    except:
        ret_data = '對不起...\nJunJun壞掉了\n暫時無法查詢QQ'
    return ret_data