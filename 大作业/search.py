# -*- coding:utf-8 -*-
from web import form
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

lucene.initVM()
print 'lucene', lucene.VERSION

def search_text(searcher, analyzer, command):
    tmp = jieba.cut(command)
    tmp = ''.join(command)
    command = tmp

   # INDEX_DIR = "IndexFiles.index"
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    STORE_DIR = "index"
    #print 'lucene', lucene.VERSION
    # base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)

    querys = BooleanQuery()
    query_content = QueryParser(Version.LUCENE_CURRENT, "urlcontent", analyzer).parse(command)
    query_title = QueryParser(Version.LUCENE_CURRENT, "contents", analyzer).parse(command)
    querys.add(query_content, BooleanClause.Occur.MUST)
    querys.add(query_title, BooleanClause.Occur.SHOULD)
    scoreDocs = searcher.search(querys, 50).scoreDocs
    print "%s total matching documents." % len(scoreDocs)
    match_count = len(scoreDocs)
    result = []
    for scoreDoc in scoreDocs:
        doc = searcher.doc(scoreDoc.doc)
        result.append({
            'title': doc.get('title'),
            'url': doc.get('url'),
            'imgurl': doc.get('imgurl'),
            'content': doc.get('urlcontent2')
        })
    return result, match_count
