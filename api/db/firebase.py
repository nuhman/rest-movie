import pyrebase
import os 

config = {
  "apiKey": os.getenv('API_KEY'),
  "authDomain": os.getenv('AUTH_DOMAIN'),
  "databaseURL": os.getenv('DATABASE_URL'),
  "storageBucket":  os.getenv('STORAGE_BUCKET')
}
fire_base= pyrebase.initialize_app(config)

database = fire_base.database()
