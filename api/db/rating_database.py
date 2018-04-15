from bson.objectid import ObjectId
from api.config.mongo import (
    user_rating_collection,
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

  def get_rating_by_user_id(self, user_id):
    '''
    Get all the movie rating of the user by user_id 
    
    Parameters:
    -----------------------------------------------
    user_id: String
      $user_ObjectId

    Returns:
    -----------------------------------------------
    dict
      {'6': 3.0, ... } // {movie_id: movie_rating, ...} 
    '''
    user_rating_document = user_rating_collection.find_one({'_id': ObjectId(user_id)})
    
    user_rating = object_id_converter(user_rating_document)
    return user_rating['ratings']

  def get_all_rating(self):
    '''
    Get all user movie ratings

    Parameters:
    ------------------------------------------------

    Returns:
    ------------------------------------------------
    dict
      {
        'ratings': 
        {
          '6': 3.0, // movie_id: movie_rating
          '21': 4.0,
          ...
        }, 
        'id': $user_ObjectId
      }
    '''
    user_rating_documents = user_rating_collection.find({})

    user_ratings = JSONEncoder(user_rating_documents, True)
    return user_ratings
    
    

if(__name__ == '__main__'):
  pass
