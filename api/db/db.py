from api.db.mongo import movie_collection
from api.db.mongo import user_collection
from bson.json_util import dumps
from bson.objectid import ObjectId
import json


def object_id_converter(item):
  '''
  converts the mongoID to string in the provided dict object

  Parameters:
  ----------------------------------------------------------
  item: dict 
    {
     '_id': ObjectId('5acf2b1935a49d0524a43f4f'), // or '_id':{'\$oid':'$objectId'},...
    }
  
  Returns:
  ----------------------------------------------------------
  dict
    {'id':'$objectId',...} or empty dict 
  '''

  if(item is None):
    return {}
  objectId = item.pop("_id", None)
  if(objectId):
    if(isinstance(objectId, (ObjectId,))):
      oid = str(objectId)
    else:
      oid = objectId.pop("$oid")
    item["id"] = oid
    return item
  return {}


def JSONEncoder(cursor, object_id_converter_flag=False):
  '''
  converts cursor object to python dict

  Parameters:
  --------------------------------------------- 
  cursor: pymongo.cursor.Cursor 
  object_id_converter_flag: boolean
  Returns:
  --------------------------------------------
  list  
  '''

  data = []
  for row in json.loads(dumps(cursor)):
    if(object_id_converter_flag):
      data.append(object_id_converter(row))
    else:
      data.append(row)
  return data


class MovieDatabase():
  def get_movies(self):
    '''
    Returns a list of movies 
    
    Parameters:
    ------------------------------------------
 
    Returns:
    ------------------------------------------
    list
      [ 
        {
          "genres": [
            "$genres_list1",
            "$genres_list2",
            "$genres_list3",
            .
            .
            .
          ],
          "id": "$objectID",
          "image": "$image_url",
          "imdbId": "0114709",
          "movieId": "1",
          "title": "Toy Story (1995)",
          "tmdbId": "862"
        },...
      ] 
    '''

    movie_list = movie_collection.find({})
    return JSONEncoder(movie_list, True)

  def set_movies(self, movies_list):
    '''
    set provided list of movies in the database.

    Parameters:
    ----------------------------------------------
    movies_list: list
    [
      {
        "genres": [
          "$genres_list1",
          "$genres_list2",
          "$genres_list3",
          .
          .
          .
        ],
        "image": "$image_url",
        "imdbId": "0114709",
        "movieId": "1",
        "title": "Toy Story (1995)",
        "tmdbId": "862"
      },...
    ]
    Returns:
    ----------------------------------------------
    null
    }
    '''

    movie_collection.insert_many(movies_list)


class UserDatabase():
  def create_user(self, user):
    '''
    creates user if does not exist in the database.

    Parameters:
    ----------------------------------------------
    user: dict
      {
        "googleId": "$googleId",
        "thumbnail" : "$user_profile_image_url",
        "username": "$username"
      }

    Returns:
    ----------------------------------------------
    dict
      {
        "googleId": "$googleId",
        "id": "$objectId",
        "thumbnail": "$user_profile_image_url",
        "username": "$username"
      }
    
    '''

    if(not self.get_user_by_google(user['googleId'])):
      inserted_id = user_collection.insert_one(user).inserted_id
      user = object_id_converter(user)
      return user
    return {}

  def get_user_by_google(self, googleId):
    '''
    get user dict object from database by googleId

    Parameters:
    ----------------------------------------------
    googleId: String
      "$googleId"
   
    Returns:
    ----------------------------------------------
    dict
      {
        "googleId": "$googleId",
        "id": "$objectId",
        "thumbnail": "$user_profile_image_url",
        "username": "$username"
      }
    '''

    return object_id_converter(user_collection.find_one({"googleId": googleId}))

  def get_user_by_id(self, id):
    '''
    get user dict object from database by objectId

    Parameters:
    ----------------------------------------------
    id: String
      "$id"
   
    Returns:
    ----------------------------------------------
    dict
      {
        "googleId": "$googleId",
        "id": "$objectId",
        "thumbnail": "$user_profile_image_url",
        "username": "$username"
      }
    '''
    
    return object_id_converter(user_collection.find_one({"_id": ObjectId(id)}))


if(__name__ == '__main__'):
  pass
