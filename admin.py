from api.db.db import MovieDatabase
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

movie_db = MovieDatabase()

def resolve_csv(path):
  return os.path.join(os.getcwd(),'movie_data',path + '.csv')


def get_image_url(imdb_id):
  r = requests.get(generate_links_imdb(imdb_id))
  soup = BeautifulSoup(r.content,'html.parser')
  poster = soup.find('div', attrs={'class':'poster'})
  soup = BeautifulSoup(str(poster),'html.parser')
  return soup.find('img').get('src')

def generate_links_imdb(imdb_id):
  if(type(imdb_id)=='int'):
    imdb_id = str(imdb_id)
  return 'http://www.imdb.com/title/tt{}/'.format(imdb_id)

def read_csv(file,no_of_rows):
  file = resolve_csv(file)
  with open(file, 'r', encoding='utf-8') as rows:
      index = 0
      data = []
      heading = rows.readline().replace('\n','').split(',')
      
      for row in rows:
        row = row.replace('\n','')
        cols = row.split(',')
        obj = {}
        for col,title in zip(cols, heading):
          if('|' in col):
            col = col.split('|')
          obj.update({title:col})
        data.append(obj)
        index+=1
        if(index == no_of_rows):
          break
      
      return data

READ_ROWS = 10
generes = read_csv('movies',READ_ROWS)
links = read_csv('links', READ_ROWS)

movies_list = []
for link, genere in zip( links, generes):
  if(link['movieId'] == genere['movieId']):
    link.update(genere)
    link['image'] = get_image_url(link['imdbId'])
    movies_list.append(link)

movie_db.set_movies(movies_list)