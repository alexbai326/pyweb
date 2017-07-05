import web
render = web.template.render('templates/')
urls = (
  '/', 'index',
  '/add', 'add'
)

class index:

    def GET(self):
        #return "Hello, world!"

        #name = 'Bob'
        #return render.index(name)

        #i = web.input(name=None)
        #return render.index(i.name)

        return render.index()

class add:

    def POST(self):
        i = web.input()
        title = i.title
        if title == "alex":
            answer = "hi alex"
            return render.add(answer)
        else:
            answer = "bye bai"
            return render.add(answer)
        #raise web.seeother('/')

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()