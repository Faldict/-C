# Experiment Report 3

###### Name: 王嘉璐
###### Class: F1503023

## Lucene
### Installation

1. Install java environment.

  ```
  sudo apt install openjdk-8
  ```

2. Install jcc.

  First, get the jcc source code.
  ```
  $ svn co http://svn.apache.org/repos/asf/lucene/pylucene/trunk/jcc jcc
  ```
  Second, config the build code. Attention, you should modify the *JDK* path to avoid errors.  
  Finally, build it!
  ```
  $ python setup.py build
  $ sudo python setup.py install
  ```

3. Install pylucene

  At first you should download the source code <a href="http://lucene.apache.org/pylucene/install.html">here</a>.  
  Then change diretory to the file and follow the instructions listed:  
    - pushd jcc
    - *edit setup.py to match your environment*
    - python setup.py build
    - sudo python setup.py install
    - popd
    - *edit Makefile to match your environment*
    - make
    - make test (look for failures)
    - sudo make install
  If there's no error, then enjoy pylucene to finish this experiment!

4. test
  Enter python interpreter, and test such code:
  ```
  import jcc
  import lucene
  lucene.initVM()
  lucene.VERSION
  ```
  As for me, I get the word "4.10.1".

### What is Lucene?

The Apache LuceneTM project develops open-source search software,
including: Lucene Core, Solr, Pylucene. It is is a high-performance,
full-featured text search engine library written entirely in Java.
It is a technology suitable for nearly any application that requires
full-text search, especially cross-platform.  

Full-text search can be divided into two process including indexing and search.

### Indexing Files

The IndexFiles class creates a Lucene Index. Let's take a look at how it does this.

The main() method parses the command-line parameters, then in
preparation for instantiating IndexWriter, opens a Directory, and
instantiates StandardAnalyzer and IndexWriterConfig.

The value of the -index command-line parameter is the name of the
filesystem directory where all index information should be stored.
If IndexFiles is invoked with a relative path given in the -index
command-line parameter, or if the -index command-line parameter is
not given, causing the default relative index path "index" to be
used, the index path will be created as a subdirectory of the
current working directory (if it does not already exist). On some
platforms, the index path may be created in a different directory
(such as the user's home directory).

The -docs command-line parameter value is the location of the
directory containing files to be indexed.

The -update command-line parameter tells IndexFiles not to delete
the index if it already exists. When -update is not given,
IndexFiles will first wipe the slate clean before indexing any
documents.

Lucene Directorys are used by the IndexWriter to store information
in the index. In addition to the FSDirectory implementation we are
using, there are several other Directory subclasses that can write
to RAM, to databases, etc.

Lucene **Analyzers** are processing pipelines that break up text into
indexed **tokens**, a.k.a. terms, and optionally perform other
operations on these tokens, e.g. downcasing, synonym insertion,
filtering out unwanted tokens, etc. The Analyzer we are using is
StandardAnalyzer, which creates tokens using the Word Break rules
from the Unicode Text Segmentation algorithm specified in Unicode
Standard Annex \#29; converts tokens to lowercase; and then filters
out stopwords. Stopwords are common language words such as articles
(a, an, the, etc.) and other tokens that may have less value for
searching. It should be noted that there are different rules for
every language, and you should use the proper analyzer for each.
Lucene currently provides Analyzers for a number of different
languages (see the javadocs under
lucene/analysis/common/src/java/org/apache/lucene/analysis).

The IndexWriterConfig instance holds all configuration for
IndexWriter. For example, we set the OpenMode to use here based on
the value of the -update command-line parameter.

Looking further down in the file, after IndexWriter is
instantiated, you should see the indexDocs() code. This recursive
function crawls the directories and creates Document objects. The
Document is simply a data object to represent the text content from
the file as well as its creation time and location. These instances
are added to the IndexWriter. If the -update command-line parameter
is given, the IndexWriterConfig OpenMode will be set to
OpenMode.CREATE_OR_APPEND, and rather than adding documents to the
index, the IndexWriter will update them in the index by attempting
to find an already-indexed document with the same identifier (in
our case, the file path serves as the identifier); deleting it from
the index if it exists; and then adding the new document to the
index.

### Searching Files

The SearchFiles class is quite simple. It primarily collaborates
with an **IndexSearcher**, **StandardAnalyzer**, (which is used in the
IndexFiles class as well) and a QueryParser. The query parser is
constructed with an analyzer used to interpret your query text in
the same way the documents are interpreted: finding word
boundaries, downcasing, and removing useless words like 'a', 'an'
and 'the'. The Query object contains the results from the
QueryParser which is passed to the searcher. Note that it's also
possible to programmatically construct a rich Query object without
using the query parser. The query parser just enables decoding the
Lucene query syntax into the corresponding Query object.

SearchFiles uses the IndexSearcher.search(query,n) method that
returns TopDocs with max n hits. The results are printed in pages,
sorted by score (i.e. relevance).

### Field

Field is the base element in a document. A field has two most
important properties: **Store** and **Index**. But one undescribed
thing is that there is no relationship between Store and Index.   

Here's an example:
```
doc.add(Field("contents", content, Field.Store.No, Field.Index.ANALYZED))
```

In our experiment, we should filter the tags before add it to the
document. The most simple method is using BeautifulSoup.

### Analyzer

Analyzer is the module to analyze and understand the documents. The
most used analyzers are: StopAnalyzer, **StandardAnalyzer**,
SimpleAnalyzer, WhitespaceAnalyzer and CJKAnalyzer.

To let lucene understand Chinese, rewrite a analyzer is not a good
idea. So I cut Chinese words into tokens and send it to
**WhitespaceAnalyzer** or **SimpleAnalyzer**.  

There's several famous Chinese word segmentation library, and I use
Jieba to finish this experiment.  

## Final Code

This is IndexFiles:

``` python
#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import jieba
import sys, os, lucene, threading, time
from datetime import datetime

from java.io import File
from org.apache.lucene.analysis.miscellaneous import LimitTokenCountAnalyzer
from org.apache.lucene.analysis.core import WhitespaceAnalyzer
from org.apache.lucene.document import Document, Field, FieldType
from org.apache.lucene.index import FieldInfo, IndexWriter, IndexWriterConfig
from org.apache.lucene.store import SimpleFSDirectory
from org.apache.lucene.util import Version

"""
This class is loosely based on the Lucene (java implementation) demo class
org.apache.lucene.demo.IndexFiles.  It will take a directory as an argument
and will index all of the files in that directory and downward recursively.
It will index on the file path, the file name and the file contents.  The
resulting Lucene index will be placed in the current directory and called
'index'.
"""

def analysis(s):
    return ' '.join(jieba.cut(s))

class Ticker(object):

    def __init__(self):
        self.tick = True

    def run(self):
        while self.tick:
            sys.stdout.write('.')
            sys.stdout.flush()
            time.sleep(1.0)

class IndexFiles(object):
    """Usage: python IndexFiles <doc_directory>"""

    def __init__(self, dialog, root, storeDir, analyzer):

        if not os.path.exists(storeDir):
            os.mkdir(storeDir)

        store = SimpleFSDirectory(File(storeDir))
        analyzer = LimitTokenCountAnalyzer(analyzer, 1048576)
        config = IndexWriterConfig(Version.LUCENE_CURRENT, analyzer)
        config.setOpenMode(IndexWriterConfig.OpenMode.CREATE)
        writer = IndexWriter(store, config)

        self.indexDocs(dialog, root, writer)
        ticker = Ticker()
        print 'commit index',
        threading.Thread(target=ticker.run).start()
        writer.commit()
        writer.close()
        ticker.tick = False
        print 'done'

    def indexDocs(self, dialog, root, writer):

        t1 = FieldType()
        t1.setIndexed(True)
        t1.setStored(True)
        t1.setTokenized(False)
        t1.setIndexOptions(FieldInfo.IndexOptions.DOCS_AND_FREQS)

        t2 = FieldType()
        t2.setIndexed(True)
        t2.setStored(False)
        t2.setTokenized(True)
        t2.setIndexOptions(FieldInfo.IndexOptions.DOCS_AND_FREQS_AND_POSITIONS)

        f = open(dialog)
        lines = f.readlines()
        for line in lines:
            info = line.split('\t')
            url = info[0]
            filename = info[1]
            title = info[2]
            print "adding", filename
            try:
                path = os.path.join(root, filename)
                file = open(path)
                contents = unicode(file.read(), 'utf-8')
                file.close()
                doc = Document()
                doc.add(Field('name', filename, t1))
                doc.add(Field('path', path, t1))
                doc.add(Field('url', url, Field.Store.YES, Field.Index.NOT_ANALYZED))
                doc.add(Field('title', title, Field.Store.YES, Field.Index.ANALYZED))
                if len(contents)>0:
                    doc.add(Field("contents", analysis(contents), t2))
                else:
                    print "warning: no content in %s" % filename
                writer.addDocument(doc)
            except Exception, e:
                print "Failed in indexDocs:", e

if __name__ == '__main__':
    """
    if len(sys.argv) < 2:
        print IndexFiles.__doc__
        sys.exit(1)
    """
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    print 'lucene', lucene.VERSION
    start = datetime.now()
    try:
        """
        base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
        IndexFiles(sys.argv[1], os.path.join(base_dir, INDEX_DIR),
                   StandardAnalyzer(Version.LUCENE_CURRENT))
                   """
        analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
        IndexFiles('index.txt', "html", "index", analyzer)
        end = datetime.now()
        print end - start
    except Exception, e:
        print "Failed: ", e
        raise e
```

And this is SearchFiles:

``` python
#!/usr/bin/env python

INDEX_DIR = "IndexFiles.index"

import sys, os, lucene
import jieba

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
def analysis(s):
    return ' '.join(jieba.cut(s))

def run(searcher, analyzer):
    while True:
        print
        print "Hit enter with no input to quit."
        command = raw_input("Query:")
        command = unicode(command, 'utf-8')
        if command == '':
            return

        print
        print "Searching for:", command
        query = QueryParser(Version.LUCENE_CURRENT, "contents",
                            analyzer).parse(analysis(command))
        scoreDocs = searcher.search(query, 50).scoreDocs
        print "%s total matching documents." % len(scoreDocs)

        for scoreDoc in scoreDocs:
            doc = searcher.doc(scoreDoc.doc)
            print 'path:', doc.get("path"), 'name:', doc.get("name"), 'url:', doc.get("url"), 'title:', doc.get("title")


if __name__ == '__main__':
	STORE_DIR = "index"
	lucene.initVM(vmargs=['-Djava.awt.headless=true'])
	print 'lucene', lucene.VERSION
	#base_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
	directory = SimpleFSDirectory(File(STORE_DIR))
	searcher = IndexSearcher(DirectoryReader.open(directory))
	analyzer = WhitespaceAnalyzer(Version.LUCENE_CURRENT)
	run(searcher, analyzer)
	del searcher
```

All the code is available, and if you want to test, run the
**test.sh** in Bash.
