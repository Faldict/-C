#!/usr/bin/env python

import requests
import json
import time

__author__ = "Faldict"
__date__ = "$2016-9-19$"
__version__ = '1.1.0'

distance = 14.26
speed = 3201
stopTime = int(time.time() * 1000)
startTime = stopTime - speed * 1000

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
