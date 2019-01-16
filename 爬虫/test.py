#!/usr/bin/python
# coding: utf-8

import json
import requests

url = "https://sns-comment.iqiyi.com/v3/comment/get_comments.action?agent_type=118&agent_version=9.11.5&authcookie=null&business_type=17&content_id=1662861200&hot_size=0&last_id=184753506321&page=&page_size=20&types=time&callback=jsonp_1547639716745_12032"

def getMoveinfo(url):
    session = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "application/json",
        "Referer": "https://www.iqiyi.com/v_19rqs2dqf0.html",
        "Origin": "https://m.iqiyi.com",
        "Host": "sns-comment.iqiyi.com",
        "Connection": "keep-alive",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,zh-TW;q=0.6",
        "Accept-Encoding": "gzip, deflate"
    }
    response = requests.get(url)
    # response.read().decode('utf8')
    if response.status_code == 200:
        print("success!")
        print(type(response.text))
        print(response.text[31:-14])
        # print(response.read())
        print(11111)
        
        t = json.loads(response.text[31:-14])
        print(t)
        print(11111)
        # print(text)
        print(response.headers['Content-Type'])
        return response.text[31:-14]
    return None

getMoveinfo(url)