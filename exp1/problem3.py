#!/usr/bin/env python
import codecs
import requests
import re
from BeautifulSoup import BeautifulSoup

def parseQiushiBaikePic(content):
	docs = {}
	nextPage = ''
	soup = BeautifulSoup(content)
	for div in soup.findAll('div', {'id' : re.compile('qiushi_tag_[\d]+')}):
		qiushi_tag_list = div.get('id','').split('_')
		qiushi_tag = qiushi_tag_list[-1]
		sentence = str(div.contents[3].contents[1].contents[1].contents[0]).decode('utf-8')
		print sentence
		imgurl = div.contents[5].contents[1].contents[1].get('src','')
		docs[qiushi_tag] = {'content': sentence, 'imgurl': imgurl}
	nextPage = 'http://www.qiushibaike.com' + soup.find('span', {'class':'next'}).parent.get('href','')
	return docs,  nextPage

def main():
	headers = {
	'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
	'Accept-Encoding': 'gzip,deflate',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7'
}
	r = requests.get("http://www.qiushibaike.com/pic/", headers)
	docs, nextPage = parseQiushiBaikePic(r.text)
	fp = codecs.open("res3.txt","w","utf-8")
	for tag in docs.values():
		txt = tag["imgurl"] + u'\t' + tag["content"] + u'\n'
		fp.write(txt)
	fp.write(str(nextPage))
	fp.close()

if __name__ == '__main__':
	main()