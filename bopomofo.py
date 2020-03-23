# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:38:44 2020

@author: xiangjun
"""

import requests
import json

def chinese_bopomofo(word):
    ret_data ='這個字應該是念做...\n'
    try:
        res = requests.get('https://www.moedict.tw/uni/'+str(word))
        jd = json.loads(res.text)
        for i in jd['heteronyms']:
            if ret_data != '':
                ret_data+='\n'
            ret_data += i['bopomofo']

    except:
        ret_data = '對不起...\nJunJunBot壞掉了\n暫時無法查詢'
    return ret_data