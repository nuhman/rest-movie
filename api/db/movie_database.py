from bson.json_util import dumps
from bson.objectid import ObjectId
import json
from api.config.mongo import movie_collection

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
    data = JSONEncoder(movie_list, True)
    return data;

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
