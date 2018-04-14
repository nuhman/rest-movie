import os
from pymongo import MongoClient

databaseUrl = 'mongodb://{}:{}@ds243059.mlab.com:43059/movie_store' \
                  .format(os.getenv('MONGO_ADMIN'),os.getenv('MONGO_PASSWORD'))

client = MongoClient(databaseUrl)

movie_collection  = client.movie_store.get_collection('movie')
user_collection = client.movie_store.get_collection('user')
user_rating_collection = client.movie_store.get_collection('user_rating')