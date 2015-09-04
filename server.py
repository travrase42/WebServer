import web



urls = (
'/', 'index'
)

class index: 
	def GET(self):
		return "Wow, such web!"
#main method 
if __name__ == '__main__':
	app = web.application(urls, globals())
	app.run()

