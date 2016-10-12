#!/usr/bin/env python

import requests

headers = {
	'Accept': '*/*',
	'Authorization': 'Basic MTU4MjExOTU4Mzc6bGVnYWR5YW4=',
	'osType': '1',
	'appVersion': '1.2.0',
	'uid': '26064',
#	'DeviceId': 'EE27A0FC-B5AC-44C6-936D-62EBFFFC6019',
#	'CustomDiviceId': 'EE27A0FC-B5AC-44C6-936D-62EBFFFC6019_iOS_sportsWorld_campus',
	'User-Agent': 'SWCampus/1.2.0(iPhone;iOS 9.3.5; Scale/3.00'
}

Host = 'http://gxapp.iydsj.com'
url = '/api/v3/26064/home/page'

r = requests.get(Host+url, headers=headers)
print r.text