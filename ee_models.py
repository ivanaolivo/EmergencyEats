from google.appengine.ext import ndb

class User(ndb.Model):
    email =  ndb.StringProperty(required=True)
    name =  ndb.StringProperty(required=True)
    dietList = ndb.StringProperty(repeated=True) #list

class FoodItem(ndb.Model):
    name = ndb.StringProperty(required=True)
    dietaryRest = ndb.StringProperty(repeated=True)
    picture = ndb.StringProperty(required=True)
    ingredients = ndb.StringProperty(required=True)
    nutrition = ndb.StringProperty(required=True)

class Restaurant(ndb.Model):
    name = ndb.StringProperty(required=True)
    picture = ndb.StringProperty(required=False)
    foodItems = ndb.KeyProperty(FoodItem, repeated=True)
