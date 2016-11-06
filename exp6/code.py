import web
from SearchFiles import run, run_img

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/result', 'search'
)


class index:
    def GET(self):
        return render.index()


class search:
    def GET(self):
        query = web.input()
        command = query['query']
        method = query['method']
        if 'page' in query.keys():
            page = int(query['page'])
        else:
            page = 1
        if method == 'img':
            result = run_img(command)
            if len(result) == 0:
                return "There is no result!"
            else:
                return render.imgresult(result)
        else:
            result = run(command)
            number = len(result)
            if len(result) < page * 20:
                result = result[(page - 1) * 20: -1]
            else:
                result = result[(page - 1) * 20: page * 20]
            return render.result(command, number, result, page)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
