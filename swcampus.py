#!/usr/bin/env python
#coding=utf-8

import requests
import json
import time

__author__ = "Faldict"
__date__ = "$2016-9-19$"
__version__ = '1.1.0'

distance = 8.57
speed = 3201
stopTime = int(time.time() * 1000)
startTime = stopTime - speed * 1000

'''
data = [
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "1",
      "endTime" : 23,
      "desc" : "光明体育场",
      "lon" : 121.43354,
      "lat" : 31.02533,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 624
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "2",
      "endTime" : 23,
      "desc" : "程及美术馆",
      "lon" : 121.43517,
      "lat" : 31.02695,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 625
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "3",
      "endTime" : 23,
      "desc" : "材料楼",
      "lon" : 121.43441,
      "lat" : 31.02956,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 626
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "4",
      "endTime" : 23,
      "desc" : "南洋北路-南洋西路口",
      "lon" : 121.43371,
      "lat" : 31.03243,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 627
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "5",
      "endTime" : 23,
      "desc" : "经三路-求实路口",
      "lon" : 121.43763,
      "lat" : 31.03137,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 628
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "6",
      "endTime" : 23,
      "desc" : "南洋北路-文俊路口",
      "lon" : 121.43934,
      "lat" : 31.03429,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 629
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "7",
      "endTime" : 23,
      "desc" : "叔同路-南洋北路口",
      "lon" : 121.44466,
      "lat" : 31.03369,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 630
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "8",
      "endTime" : 23,
      "desc" : "文治大道-宣怀大道口",
      "lon" : 121.45011,
      "lat" : 31.0331,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 631
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "9",
      "endTime" : 23,
      "desc" : "环一路-思源东路口",
      "lon" : 121.45097,
      "lat" : 31.03067,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 632
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "10",
      "endTime" : 23,
      "desc" : "综合办公楼",
      "lon" : 121.45487,
      "lat" : 31.03183,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 633
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "11",
      "endTime" : 23,
      "desc" : "航空航天学院",
      "lon" : 121.45539,
      "lat" : 31.02995,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 634
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "12",
      "endTime" : 23,
      "desc" : "无线电电子研究所",
      "lon" : 121.45254,
      "lat" : 31.02947,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 635
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "13",
      "endTime" : 23,
      "desc" : "软件学院实验室",
      "lon" : 121.44922,
      "lat" : 31.02814,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 636
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "14",
      "endTime" : 23,
      "desc" : "中意绿色能源实验室",
      "lon" : 121.44551,
      "lat" : 31.02747,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 637
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "15",
      "endTime" : 23,
      "desc" : "文俊路-思源南路口",
      "lon" : 121.44159,
      "lat" : 31.02896,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 638
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "16",
      "endTime" : 23,
      "desc" : "南洋南路-精勤路口",
      "lon" : 121.43976,
      "lat" : 31.02585,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 639
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "17",
      "endTime" : 23,
      "desc" : "菁菁广场",
      "lon" : 121.43696,
      "lat" : 31.02494,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 640
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "18",
      "endTime" : 23,
      "desc" : "宣怀大道-叔同路口",
      "lon" : 121.4453,
      "lat" : 31.03211,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 641
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "19",
      "endTime" : 23,
      "desc" : "环一桥-宣怀大道口",
      "lon" : 121.4478,
      "lat" : 31.03296,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 642
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "20",
      "endTime" : 23,
      "desc" : "第五食堂",
      "lon" : 121.44879,
      "lat" : 31.02999,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 643
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "21",
      "endTime" : 23,
      "desc" : "蔬果每日",
      "lon" : 121.43755,
      "lat" : 31.0291,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 644
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "22",
      "endTime" : 23,
      "desc" : "精勤路-思源南路口",
      "lon" : 121.43895,
      "lat" : 31.02822,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 645
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "23",
      "endTime" : 23,
      "desc" : "学生公寓15楼",
      "lon" : 121.44301,
      "lat" : 31.03017,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 646
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "24",
      "endTime" : 23,
      "desc" : "宣怀大道-元培路",
      "lon" : 121.44371,
      "lat" : 31.03161,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 647
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "25",
      "endTime" : 23,
      "desc" : "东中院",
      "lon" : 121.44319,
      "lat" : 31.0287,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 648
    },
    {
      "runMode" : 1,
      "unid" : 301,
      "serialNum" : "26",
      "endTime" : 23,
      "desc" : "叔同路-思源南路口",
      "lon" : 121.44655,
      "lat" : 31.02929,
      "isFixed" : 0,
      "fromTime" : 0,
      "pid" : 649
    }
]
'''


headers = {
	'Accept': '*/*',
	'Authorization': 'Basic MTU4MjExOTU4Mzc6bGVnYWR5YW4=',
	'osType': '1',
	'uid': '22646',
	'appVersion': '1.2.0',
	'DevicedId': 'EE27A0FC-B5AC-44C^-936D-62EBFFFC6019',
	'CustomDiviceId': 'EE27A0FC-B5AC-44C^-936D-62EBFFFC6019_iOS_sportsWorld_campus',
	'User-Agent': 'SWCampus/1.2.0(iPhone;iOS 9.3.5; Scale/3.00'
}

payload = {
	"totalDis": distance,
	"sportType": 1,
	"speed": 9,
	"fivePointJson" : "",
	"selDistance" : 5,
	"totalTime" : speed,
	"allLocJson" :  "{}",
	"complete" : True,
	"unCompleteReason" : 4,
	"startTime" : startTime,
	"stopTime" : stopTime
}

#payload["fivePointJson"] = "{\n \"useZip\" : false,\n \"fivePointJson\" : \"[{\\\"flag\\\": \\\"147427798000\\\", \\\"isPass\\\": true, \\\"lat\\\": \\\"31.029290\\\", \\\"lon\\\": \\\"121.446550\\\", \\\"isFixed\\\": \\\"0\\\"},{\\\"flag\\\": \\\"147427798000\\\", \\\"isPass\\\": true, \\\"lat\\\": \\\"31.028140\\\", \\\"lon\\\": \\\"121.449220\\\", \\\"isFixed\\\": \\\"0\\\"},{\\\"flag\\\": \\\"147427798000\\\", \\\"isPass\\\": true, \\\"lat\\\": \\\"31.029470\\\", \\\"lon\\\": \\\"121.452540\\\", \\\"isFixed\\\": \\\"0\\\"},{\\\"flag\\\": \\\"147427798000\\\", \\\"isPass\\\": true, \\\"lat\\\": \\\"31.027470\\\", \\\"lon\\\": \\\"121.445510\\\", \\\"isFixed\\\": \\\"1\\\"},{\\\"flag\\\": \\\"147427798000\\\", \\\"isPass\\\": true, \\\"lat\\\": \\\"31.028220\\\", \\\"lon\\\": \\\"121.438950\\\", \\\"isFixed\\\": \\\"0\\\"}]\"\n}"
#payload["allLocJson"] = "{\n \"useZip\" : false,\n \"allLocJson\" : \"[]\"\n}"



Host = 'http://gxapp.iydsj.com'
url = '/api/v2/users/22646/running_records/add'

r = requests.post(Host+url, headers=headers, json=payload)
print r.text
