import os
from pymongo import MongoClient


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


databaseUrl = 'mongodb://{}:{}@ds243059.mlab.com:43059/movie_store' \
    .format(os.getenv('MONGO_ADMIN'), os.getenv('MONGO_PASSWORD'))

client = MongoClient(databaseUrl)

movie_collection = client.movie_store.get_collection('movie')
user_collection = client.movie_store.get_collection('user')
user_rating_collection = client.movie_store.get_collection('user_rating')
