import web
import xml.etree.ElementTree as ET



urls = (
	'/users', 'list_users',
	'/users/(.*)', 'get_user'
)

app = web.application(urls, globals())

class list_users:        
	def GET(self):
		output = 'users:[serdar,dergi]';
		
		return output

class get_user:
	def GET(self, user):
		return '['+user+']'

if __name__ == "__main__":
	app.run()
