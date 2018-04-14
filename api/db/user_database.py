from bson.json_util import dumps
from bson.objectid import ObjectId
import json
from api.config.mongo import user_collection


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
