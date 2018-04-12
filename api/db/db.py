from api.db.mongo import movie_collection
from api.db.mongo import user_collection
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

def ObjectIDConverter(item):
  if(item is None):
    return None
  objectId = item.pop("_id",None)
  if(objectId):
    if(isinstance(objectId, (ObjectId,))):
      oid = str(objectId)
    else:
      oid = objectId.pop("$oid")
    item["id"] = oid
    return item
  return None

def JSONEncoder(cursor):
  data = []
  for row in json.loads(dumps(cursor)):
    data.append(row)
  return data
    

class MovieDatabase():
  def get_movies(self, user):
    movie_list = movie_collection.find({})
    return JSONEncoder(movie_list)

  def set_movies(self, movies_list):
      movie_collection.insert_many(movies_list)

class UserDatabase():
  def create_user(self, user):
    if(not self.get_user_by_google(user['googleId'])):
      inserted_id = user_collection.insert_one(user).inserted_id
      user = ObjectIDConverter(user)
      return user
    return {};
  
  def get_user_by_google(self, googleId):
    return ObjectIDConverter(user_collection.find_one({"googleId":googleId})) or {}


  def get_user_by_id(self, id):
    return ObjectIDConverter(user_collection.find_one({"_id": ObjectId(id)})) or {}

if(__name__ == '__main__'):
  pass