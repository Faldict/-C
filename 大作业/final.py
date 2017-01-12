#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene,cv2
import searchEngine
from java.io import File
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.util import Version

"""
This script is loosely based on the Lucene (java implementation) demo class 
org.apache.lucene.demo.SearchFiles.  It will prompt for a search query, then it
will search the Lucene index in the current directory called 'index' for the
search query entered against the 'contents' field.  It will then display the
'path' and 'name' fields for each of the hits it finds in the index.  Note that
search.close() is currently commented out because it causes a stack overflow in
some cases.
"""
def run(searcher, analyzer,image):
    result=searchEngine.find_name(image)
    final=[]
    for i in range(10):
        command=result[i]
        query = QueryParser(Version.LUCENE_CURRENT, "picname",analyzer).parse(command)
        scoreDocs = searcher.search(query, 50).scoreDocs
        
        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            final.append({
                'title': doc.get('title'),
                'url': doc.get('url'),
                'pic_url': doc.get('pic_url'),
                'Content': doc.get('title'),
                'description': doc.get('description'),
                'price': doc.get('price')
            })
    return final


def search_img(image):
    img = cv2.imread(image)
    vm_env = lucene.getVMEnv()
    vm_env.attachCurrentThread()
    STORE_DIR = "index"
    directory = SimpleFSDirectory(File(STORE_DIR))
    searcher = IndexSearcher(DirectoryReader.open(directory))
    analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
    result=run(searcher, analyzer,img)
    return result
    del searcher
