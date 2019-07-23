import webapp2
import jinja2
import os

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = the_jinja_env.get_template('loginpage.html')
        self.response.write(template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
