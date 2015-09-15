import web
render = web.template.render('templates/', base = 'base')


urls = (
	'/rainbowTrout', 'index',
	'/brownTrout', 'brownTrout'
)
class index:
	def GET(self):
		return render.index();

class brownTrout:
	def GET(self):
		return render.brownTrout();


#main method
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()
