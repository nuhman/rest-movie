from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
from dotenv import load_dotenv

load_dotenv()

from api.engine.movies import get_movies
from api.db.db import UserDatabase
import os 


app = Flask(__name__)
CORS(app)

@app.route('/movies/list/<user>')
def defaultMovies(user):
  return jsonify(get_movies(user))

@app.route('/users/create/', methods=['POST'])
def create_user():
  user = request.json
  user = user_db.create_user(user)
  return jsonify(user)

@app.route('/users/get-google/', methods=['POST'])
def get_user_by_google(): 
  googleId = request.json['googleId']
  user = user_db.get_user_by_google(googleId)
  return jsonify(user)

@app.route('/users/get-id/', methods=['POST'])
def get_user_by_id(): 
  id = request.json['id']
  user = user_db.get_user_by_id(id)
  return jsonify(user)