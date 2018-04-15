from bson.objectid import ObjectId
from api.config.mongo import (
  movie_collection,
  object_id_converter,
  JSONEncoder
)


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
    data = JSONEncoder(movie_list, True)
    return data

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


if(__name__ == '__main__'):
  pass
