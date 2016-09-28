#!/usr/bin/env python

__author__ = "Wang Jialu"
__date__ = "2016-09-22"

import Queue
import threading
import time
from BeautifulSoup import BeautifulSoup
import urllib2
import re 
import urlparse
import os
import urllib
import string

q = Queue.Queue()
threadLock = threading.Lock()
crawled = []
count = 0


class myThread (threading.Thread):
	def __init__(self, threadID):
		threading.Thread.__init__(self)
		self.threadID = threadID
#		self.url = page
#		self.method = method
#		self.count = max_page

	def run(self):
		crawl()
		

def valid_filename(s):
	valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
	s = ''.join(c for c in s if c in valid_chars)
	return s

def get_page(page):
	content = ''
	try:
		req = urllib2.urlopen(page)
	except:
		pass
	else:
		content = req.read()
	return content

def get_all_links(content, page):
	links = []
	soup = BeautifulSoup(content)
	for a in soup.findAll('a', {'href': re.compile('^http|^/')}):
		url = a.get('href')
		if url[0] == '/':
			url = urlparse.urljoin(page, url)
		links.append(url) 
	return links

def union_queue(q, links):
	for url in links:
		if url not in crawled:
			threadLock.acquire()
			q.put(url)
			threadLock.release()


def add_page_to_folder(page, content):
	index_filename = 'index.txt'
	folder = 'html'
	filename = valid_filename(page)
	index = open(index_filename, 'a')
	index.write(page.encode('ascii', 'ignore') + '\t' + filename + '\n')
	index.close()
	if not os.path.exists(folder):
		os.mkdir(folder)
	f = open(os.path.join(folder, filename), 'w')
	f.write(content)
	f.close

def crawl():
	if count > 1000:
		return
	if q.empty():
		time.sleep(1)
		crawl()
	else:
		threadLock.acquire()
		url = q.get()
		q.pop()
		threadLock.release()
		if url in crawled:
			crawl()
		else:
			content = get_page(url)
			add_page_to_folder(url, content)
			links = get_all_links(url)
			union_queue(q, links)
			crawled.append(url)
			count += 1




