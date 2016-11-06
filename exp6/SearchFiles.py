#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys
import os
import lucene
import jieba

from java.io import File
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version
from org.apache.lucene.search.highlight import Highlighter
from org.apache.lucene.search.highlight import QueryScorer
from org.apache.lucene.search.highlight import SimpleHTMLFormatter
from org.apache.lucene.search import BooleanQuery
from org.apache.lucene.search import BooleanClause

"""
This script is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""


lucene.initVM()
print 'lucene', lucene.VERSION


def analysis(s):
    return ' '.join(jieba.cut(s))


def run(command):
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    STORE_DIR = "index1"
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
    query = QueryParser(Version.LUCENE_CURRENT, "contents", analyzer).parse(analysis(command))
    HighlightFormatter = SimpleHTMLFormatter()
    highlighter = Highlighter(HighlightFormatter, QueryScorer(query))
    scoreDocs = searcher.search(query, 500).scoreDocs
    print "%s total matching documents." % len(scoreDocs)
    result = []
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        print 'path:', doc.get("path"), 'name:', doc.get("name"), 'url:', doc.get("url"), 'title:', doc.get("title")
        text = doc.get('contents')
        highLightText = highlighter.getBestFragment(analyzer, "contents", text)
        if highLightText != None: 
            highLightText = ''.join(highLightText.split(' '))
        data = {}
        data['url'] = doc.get("url")
        data['title'] = doc.get('title')
        data['highlight'] = highLightText
        result.append(data)
    return result


def run_img(command):
        vm_env = lucene.getVMEnv()
        vm_env.attachCurrentThread()
        STORE_DIR = "index2"
        directory = SimpleFSDirectory(File(STORE_DIR))
        searcher = IndexSearcher(DirectoryReader.open(directory))
        analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
        querys = BooleanQuery()
        query_content = QueryParser(Version.LUCENE_CURRENT, "urlcontent", analyzer).parse(command)
        query_title = QueryParser(Version.LUCENE_CURRENT, "title", analyzer).parse(command)
        querys.add(query_content, BooleanClause.Occur.SHOULD)
        querys.add(query_title, BooleanClause.Occur.SHOULD)
        scoreDocs = searcher.search(querys, 50).scoreDocs
        if len(scoreDocs) == 0:
            print "WARNING: No result"
        result = []
        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print doc.get("title")
            data = {}
            data['title'] = doc.get('title')
            data['url'] = doc.get('url')
            data['imgurl'] = doc.get('imgurl')
            result.append(data)
        return result