import web
import cv2
import lsh
import search
import os

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/image', 'image'
)

# init dataset
db = lsh.build_dataset()

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
    def POST(self):
        query = web.input()
        text = query['text']
        x = web.input(myfile={})
        name = x['myfile'].filename
        content = x['myfile'].value
        print name
        if name != '' and content != '':
            img = upload(name, content)
            return render.image(text, img)
        else:
            return render.image(text, "")


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
