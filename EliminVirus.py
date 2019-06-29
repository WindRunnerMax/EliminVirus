#!/usr/bin/python 
# -*- coding: utf-8 -*-

import time
import requests
import re
import os
import json
import datetime
import hashlib

openid = ""
money = "1000000000"
diamond = "5000"

class EliminVirus(object):
    """docstring for EliminVirus"""
    def __init__(self):
        super(EliminVirus, self).__init__()
        self.__headers = {
            "charset": "utf-8",
            "referer": "https://servicewechat.com/wxa2c324b63b2a9e5e/70/page-frame.html",
            "content-type": "application/x-www-form-urlencoded",
            "User-Agent": "MicroMessenger/6.6.7.1320(0x26060734) NetType/4G Language/en",
            "Host": "wxwyjh.chiji-h5.com",
            "Connection": "Keep-Alive"
        }
        self.__initData = { 
            "plat" : "wx",
            "time" : int(round(time.time() * 1000)),
            "openid" : openid
        }

    def get_sign(self,data):
        m2 = hashlib.md5()
        data["wx_appid"] = "wxa2c324b63b2a9e5e"
        data["wx_secret"] = "8fbd540d0b23197df1d5095f0d6ee46d"
        sortedData = dict(sorted(data.items()))
        string = ""
        for x in sortedData:
            string += (x + "=" + str(data[x]) + "&")
        string = string[:-1]
        m2.update(string.encode("utf8"))   
        return (m2.hexdigest())

    def run(self):
        session = requests.Session()
        sign = self.get_sign(self.__initData.copy())
        subInfo = self.__initData.copy()
        subInfo['sign'] = sign
        url = "https://wxwyjh.chiji-h5.com/api/archive/get"
        req = session.post(url , data=json.dumps(subInfo), timeout=5 ,headers = self.__headers)
        userInfo = json.loads(req.text)
        userInfo['data']['record'] = json.loads(userInfo['data']['record'])
        userInfo['data']['record']['money'] = money
        userInfo['data']['record']['zuanShi'] = diamond
        url = "https://wxwyjh.chiji-h5.com/api/archive/upload"
        subInfo2 = self.__initData.copy()
        subInfo2['time'] = int(round(time.time() * 1000)) + 100
        subInfo2['record'] = json.dumps(userInfo['data']['record'])
        sign = self.get_sign(subInfo2)
        subInfo2['sign'] = sign
        req = session.post(url , data=json.dumps(subInfo2), timeout=5 ,headers = self.__headers)
        print(req.text)

if __name__ == '__main__':
    eliminVirus = EliminVirus()
    eliminVirus.run()
    