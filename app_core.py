#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# import library Start
from __future__ import unicode_literals
from flask import Flask, request, abort, render_template
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ConfirmTemplate, PostbackTemplateAction, MessageTemplateAction,LocationMessage,FlexSendMessage

import os
import sys
import json
import pprint
import requests
import base64
import time
import random
import os

from function import weather,bopomofo


# import library end


app = Flask(__name__)

# LINE 聊天機器人的基本資料
line_bot_api = LineBotApi('gOINXGXIdMfl5iDgykoahC14wN/XyqT6Eqf+wZa0G+VzhQ9m8YWV17Yod8CMoWibUu8QJFChAn/TGLEZdfW+7vMgq9cclC81XEJolM8doj8J98I57vIOxjsPt1ja0UFDL3/vSYfycvJv5uXLozhadAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('acaf7549c92065062bde9dd1a6c04379')

@app.route("/")
def home():
    return render_template("home.html")
    
@app.route("/from_start")
def from_start():
    return render_template("from_start.html")

# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def echo(event):
    def ltext(reply):
        return TextSendMessage(text=reply)
    body = request.get_data(as_text=True)
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
                 
        event = json.loads(body)['events'][0]
        
        try:
            content_type = event['message']['type']
            reply_to = event['replyToken']
            say = event['message']['text']
            command = say.lower()
        except:
            content_type = event['message']['type']
            reply_to = event['replyToken']
            msg_id = event['message']['id']
    
        if content_type == 'text':#普通文字
            if command == 'ㄩㄇ':
                line_bot_api.reply_message(reply_to,ltext('不ㄩ'))
            elif command =='安安':
                line_bot_api.reply_message(reply_to,ltext('安安Hello'))
            elif command =='是在哈囉':
                line_bot_api.reply_message(reply_to,ltext('我就爛!'))
            elif command =='你好':
                line_bot_api.reply_message(reply_to,ltext('哈囉尼好'))
            elif command =='help':
                rp = '嗨嗨!!!\n'+\
                '歡迎使用JunJunbot\n'+\
                '使用JunJunbot之前\n'+\
                '敬請注意以下幾件事情\n'+\
                '1.請勿拍打餵食\n'+\
                '2.別對我講怪怪的話(?\n'+\
                '3.本機器人可能會不定期維護\n'+\
                '4.查詢指令請輸入「command」\n'+\
                '5.查看作者請輸入「about」\n'+\
                '謝謝您的合作:)'
                line_bot_api.reply_message(reply_to,ltext(rp))
                #print (rp)
            elif command =='command':
                rp ='1.輸入「天氣」可以查詢你所在位置的天氣\n'+\
                    '2.輸入「注音：字」可查詢該字的注音\n'+\
                    '功能還在開發中，期待大家來發掘\n'+\
                    '謝謝大家！！'
                line_bot_api.reply_message(reply_to,ltext(rp))
                #print (rp)        
            elif command =='about':
                rp ='安安!!\n'+'我叫做張翔峻\n'+\
                    '目前就讀北科大電機工程系\n'+\
                    '如果對於這個APP有任何建議\n'+\
                    '請各位email給我\n'+\
                    'a26576711@gmail.com\n'+\
                    '感謝各位的支持!!'
                line_bot_api.reply_message(reply_to,ltext(rp))
            elif '天氣' in command:
                line_bot_api.reply_message(reply_to, ltext('請傳位置訊息給我'))
            elif '注音' in command:
                command = command[command.find("：")+1:]
                line_bot_api.reply_message(reply_to,ltext(bopomofo.chinese_bopomofo(command)))
            else:
                rp = '對不起...\n'+\
                     'JunJun沒教我這是什麼意思嗚嗚...\n'+\
                     '請使用「help」來看JunJunbot能幹嘛'
                line_bot_api.reply_message(reply_to,ltext(rp))
                #line_bot_api.reply_message(reply_to,ltext(str(body)))

@handler.add(MessageEvent, message=LocationMessage)
def location(event):
    def ltext(reply):
        return TextSendMessage(text=reply)
    body = request.get_data(as_text=True)
    if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
        
        event = json.loads(body)['events'][0]
        
        try:
            content_type = event['message']['type']
            reply_to = event['replyToken']
            say = event['message']['text']
            command = say.lower()
        except:
            content_type = event['message']['type']
            reply_to = event['replyToken']
            msg_id = event['message']['id']
            
        if content_type == 'location': #定位
            lat = event['message']['latitude']
            lon = event['message']['longitude']
            line_bot_api.reply_message(reply_to, ltext(weather.get_weather(lat,lon)))

if __name__ == "__main__":
    app.run()

