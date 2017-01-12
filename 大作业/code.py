import web
import cv2
import sea
import os, lucene
import final


import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/index', 'index',
    '/image', 'image'
)


# deal with the upload img
def upload(name, content):
    root = 'static/upload/'
    if not os.path.exists(root):
        os.mkdir(root)
    filename = root + name

    f = open(filename, "w")
    f.write(content)
    return filename


class index:
    def GET(self):
        return render.index()


class image:
    def GET(self):
        query = web.input()
        text = query['text']
        count, result = sea.func_img(text)
        return render.image(text, result, count, '')

    def POST(self):
        query = web.input()
        x = web.input(myfile={})
        name = x['myfile'].filename
        content = x['myfile'].value

        img = upload(name, content)
        result = final.search_img(img)
        count = len(result)
        return render.image('', result, count, img)



if __name__ == '__main__':
    lucene.initVM(vmargs=['-Djava.awt.headless=true'])
    app = web.application(urls, globals())
    app.run()
