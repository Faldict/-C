#!/usr/bin/env python

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
import codecs

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

q = Queue.Queue()
threadLock = threading.Lock()
crawled = []
threads = []
count = 0
exitFlag = 0


class myThread (threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.threadID = threadID
        # self.url = page
        # self.method = method
        # self.count = max_page

    def run(self):
        print "[START]Running Thread", self.threadID
        crawl(self.threadID)
        print "[STOP]Ending Thread", self.threadID


def valid_filename(s):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    s = ''.join(c for c in s if c in valid_chars)
    return s


def get_page(page):
    content = ''
    try:
        r = urllib2.urlopen(page, timeout=1)
    except Exception, e:
        print "WARNING:", Exception, e
    else:
        content = r.read()
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
    print "[INFO]Finished to add urls, now there are", q.qsize(), "urls in the queue!"


def add_page_to_folder(page, content):
    index_filename = 'index.txt'
    folder = 'html'
    filename = valid_filename(page)
    soup = BeautifulSoup(content)
    if soup.title:
        title = soup.title.string
    else:
        title = page
    index = codecs.open(index_filename, 'a', 'utf-8')
    index.write(page + '\t' + filename + '\t' + title + '\n')
    index.close()
    if not os.path.exists(folder):
        os.mkdir(folder)
    f = codecs.open(os.path.join(folder, filename), 'w', 'utf-8')
    f.write(content)
    f.close


def crawl(id):
    global count
    while count < 5000:
        if q.empty():
            time.sleep(1)
        elif count > 0 and q.empty():
            print "[WARNING]All the urls are crawled!"
            break
        else:
            threadLock.acquire()
            url = q.get()
            threadLock.release()
            if url[-3:] == 'apk':
                pass
            else:
                print "[INFO]Thread", id, "is crawling", url
                crawled.append(url)
                content = get_page(url)
                add_page_to_folder(url, content)
                links = get_all_links(content, url)
                union_queue(q, links)
                count += 1


def main():
	print "main thread is running"
	q.put("http://www.jianshu.com/")
	for i in range(10):
		t = myThread(i)
		threads.append(t)
		t.start()
	for i in range(10):
		threads[i].join()
	print "Exit Main Thread"

main()
