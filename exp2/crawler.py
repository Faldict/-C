#!/usr/bin/env python

def bbs_set(id, pw, text):
	import requests
	from BeautifulSoup import BeautifulSoup
	from requests.auth import HTTPBasicAuth
	import urllib, urllib2 ,cookielib
	host = 'https://bbs.sjtu.edu.cn'
#	jar = requests.cookies.RequestsCookieJar()
	payload = {'id': id, 'pw': pw, 'submit':'login'}
#	s = requests.post(host+'/bbslogin', data = payload)
#	r = requests.get(host+'/bbsleftnew', cookies = jar)
#	print 'Faldict' in r.text

	cj = cookielib.CookieJar()
	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
	urllib2.install_opener(opener)
	postdata = urllib.urlencode(payload)
	req = urllib2.Request(url='https://bbs.sjtu.edu.cn/bbslogin', data=postdata)
	response = urllib2.urlopen(req)
	response = urllib2.urlopen('https://bbs.sjtu.edu.cn/bbsleftnew')
	print id in response.read()
	postdata = urllib.urlencode({
		'type': 'update',
		'text': text
		})
	req = urllib2.Request(url='https://bbs.sjtu.edu.cn/bbsplan', data=postdata)
	response = urllib2.urlopen(req)
	response = urllib2.urlopen('https://bbs.sjtu.edu.cn/bbsplan')
	content = response.read()
	soup = BeautifulSoup(content)
	print soup.find('textarea').string



id = 'Faldict'
pw = 'legadyan'
text = 'spider'


bbs_set(id,pw,text)