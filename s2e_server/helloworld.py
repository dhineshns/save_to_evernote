import webapp2
import sys
sys.path.insert(0, 'lib')


from evernote.api.client import EvernoteClient
import evernote.edam.type.ttypes as Types



class MainPage(webapp2.RequestHandler):
    def get(self):
		dev_token = "S=s1:U=8f597:E=14f8fa7d7c0:C=14837f6a8a8:P=1cd:A=en-devtoken:V=2:H=63d9d181619d497df03159898990bce5"
		client = EvernoteClient(token=dev_token)
		userStore = client.get_user_store()
		user = userStore.getUser()
		self.response.headers['Content-Type'] = 'text/plain'
		self.response.write(user.username)

		noteStore = client.get_note_store()
		note = Types.Note()
		note.title = "I'm a test note! Baby"
		note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
		note.content += '<en-note>Hello, world!</en-note>'
		note = noteStore.createNote(note)
class Guestbook(webapp2.RequestHandler):
	def post(self):
		dev_token = "S=s1:U=8f597:E=14f8fa7d7c0:C=14837f6a8a8:P=1cd:A=en-devtoken:V=2:H=63d9d181619d497df03159898990bce5"
		client = EvernoteClient(token=dev_token)
		data = self.request.get('note')

		noteStore = client.get_note_store()
		note = Types.Note()
		note.title = "Chrome to Evernote"
		note.content = '<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
		note.content += '<en-note>' + str(data) +'</en-note>'
		note = noteStore.createNote(note)

		self.response.write(data)


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign', Guestbook)
], debug=True)


