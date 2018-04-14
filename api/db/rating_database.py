from bson.json_util import dumps
from bson.objectid import ObjectId
import json
from api.config.mongo import (
  movie_collection,
  object_id_converter,
  JSONEncoder
)


class RatingDatabase():
  def push_new_rating(self, user_id, movie_id, movie_rating):
    '''
    Add movie ratings to the user_ratings_collection

    Parameters:
    -----------------------------------------------
    user_id: String 
      Object_id of the user
    movie_id: String 
      id of the movie
    movie_ratings: Float  
      user rating in float

    Returns:
    -----------------------------------------------
    null

    '''
    payload = {
        "ratings.{}".format(movie_id): movie_rating
    }

    user_rating_collection.update_one({'_id': ObjectId(user_id)},
                                      {'$set': payload}, upsert=True)

  def push_new_rating_batch(self, user_id,  movie_ratings_list):
    '''
    Add movie ratings to the user_ratings_collection

    Parameters:
    -----------------------------------------------
    user_id: String 
      ObjectId of the user
    movie_ratings_list: dict  
      {'ratings.31': '2.5', ...}
    Returns:
    -----------------------------------------------
    null

    '''
    user_rating_collection.update_many({'_id': ObjectId(user_id)},
                                       {'$set': movie_ratings_list}, upsert=True)


if(__name__ == '__main__'):
  pass
