import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello!!")
        html = open("home.html").read()
        self.response.write(html)


start = webapp2.WSGIApplication([
    ('/', MainHandler)
    ]   , debug = True)
