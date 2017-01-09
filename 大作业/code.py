import web

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/text', 'text',
    '/image', 'image'
)

class index:
    def GET(self):
        return render.index()


class text:
    def GET(self):
        query = web.input()
        return render.text()


class image:
    def GET(self):
        query = web.input()
        return render.image()


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
