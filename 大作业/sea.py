# -*- coding:utf-8 -*-
import urllib2
import os



import sys, os, lucene
import cgi
from java.io import File
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.search import BooleanQuery
from org.apache.lucene.search import BooleanClause
from org.apache.lucene.search.highlight import Highlighter
from org.apache.lucene.search.highlight import QueryScorer
from org.apache.lucene.search.highlight import SimpleHTMLFormatter
import jieba
prefixHTML = "<font color='red'>"
suffixHTML = "</font>"

def work(searcher, analyzer,command, low=None,high=None):
    global prefixHTML
    global suffixHTML
    if command == '':
        return 0, []
    tmp = jieba.cut(command)
    if command == '':
        return 0, []
    tmp = jieba.cut(command)
    tmp = ''.join(command)
    command = tmp
    query = QueryParser(Version.LUCENE_CURRENT, "contents", analyzer).parse(command)
    scoreDocs = searcher.search(query, 50).scoreDocs
    print "%s total matching documents." % len(scoreDocs)
    simpleHTMLFormatter = SimpleHTMLFormatter(prefixHTML, suffixHTML)
    highlighter = Highlighter(simpleHTMLFormatter, QueryScorer(query))
    result=[]
    match_count = len(scoreDocs)
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        text = doc.get("contents")
        content = highlighter.getBestFragment(analyzer, "contents", text)
        if (low == None) and (high == None):
            result.append(
                {"url": doc.get('url'), "Content": content, "pic_url": doc.get('pic_url'), "title": doc.get('title'),
                 "price": doc.get('price'), "description": doc.get('description')})
        elif  (low != None and high != None):
            if doc.get('price')>=int(low) and doc.get('price')<=int(high) :
                result.append({"url": doc.get('url'), "Content": content, "pic_url": doc.get('pic_url'),
                               "title": doc.get('title'), "price": doc.get('price'),
                               "description": doc.get('description')})
        elif  (low==None and high !=None):
            if doc.get('price')<=int(high) :
                result.append({"url": doc.get('url'), "Content": content, "pic_url": doc.get('pic_url'),
                               "title": doc.get('title'), "price": doc.get('price'),
                               "description": doc.get('description')})
        else:
            if doc.get('price')>=int(low) :
                result.append({"url": doc.get('url'), "Content": content, "pic_url": doc.get('pic_url'),
                               "title": doc.get('title'), "price": doc.get('price'),
                               "description": doc.get('description')})
    result = sorted(result, key =lambda x: float(x["price"]),reverse=True)

    return match_count, result


def func_img(command):
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    STORE_DIR = "index"
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
    match_count,result=work(searcher,analyzer,command)
    del searcher
    return match_count,result
