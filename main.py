import webapp2
import jinja2
import os
from ee_models import User, FoodItem, Restaurant

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class LoginHandler(webapp2.RequestHandler):
    def get(self):
        login_template = the_jinja_env.get_template('templates/loginpage.html')
        self.response.write(login_template.render())

restaurant_dict = {
    'Rest1': 'Panera',
    'Rest2': 'McDonalds',
    'Rest3': 'Chipotle',
}

class RestaurantHandler(webapp2.RequestHandler):
    def get(self):
        restaurant_list = Restaurant.query().fetch()
        restaurant_template = the_jinja_env.get_template('templates/restaurants.html')
        self.response.write(restaurant_template.render(restaurant_dict))



app = webapp2.WSGIApplication([
    ('/', LoginHandler),
    ('/restaurants', RestaurantHandler),
], debug=True)
