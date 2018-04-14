import requests
from bs4 import BeautifulSoup
import os
from bson.objectid import ObjectId
import click

from dotenv import load_dotenv
load_dotenv(verbose=True)

from api.db.movie_database import MovieDatabase
from api.db.rating_database import RatingDatabase

movie_db = MovieDatabase()
ratings_db = RatingDatabase()


def resolve_csv(path):
  return os.path.join(os.getcwd(), 'movie_data', path + '.csv')


def get_image_url(imdb_id):
  r = requests.get(generate_links_imdb(imdb_id))
  soup = BeautifulSoup(r.content, 'html.parser')
  poster = soup.find('div', attrs={'class': 'poster'})
  soup = BeautifulSoup(str(poster), 'html.parser')
  return soup.find('img').get('src')


def generate_links_imdb(imdb_id):
  if(type(imdb_id) == 'int'):
    imdb_id = str(imdb_id)
  return 'http://www.imdb.com/title/tt{}/'.format(imdb_id)


def read_csv(file, no_of_rows=-1):
  resolved_file = resolve_csv(file)
  with open(resolved_file, 'r', encoding='utf-8') as rows:
      index = 0
      data = []
      heading = rows.readline().replace('\n', '').split(',')
      progressbar_length = no_of_rows
      if no_of_rows is -1:
        progressbar_length = None
      with click.progressbar(rows, 
                             label='parsing %s.csv' % file, 
                             length = progressbar_length) as bars:
        for row in bars:
          row = row.replace('\n', '')
          cols = row.split(',')
          obj = {}
          for col, title in zip(cols, heading):
            if('|' in col):
              col = col.split('|')
            obj.update({title: col})
          data.append(obj)
          index += 1
          if(index == no_of_rows):
            break

      return data


def upload_movies_list(READ_ROWS):
  movies = read_csv('movies', READ_ROWS)
  links = read_csv('links', READ_ROWS)

  movies_list = []
  with click.progressbar(zip(links, movies),
                         label='paking movies list',
                         length=len(movies)) as bars:
    for link, movie in bars:
      if(link['movieId'] == movie['movieId']):
        link.update(movie)
        link['image'] = get_image_url(link['imdbId'])
        movies_list.append(link)

  click.echo(click.style('uploading movies list'))
  movie_db.set_movies(movies_list)

def upload_movies_rating(READ_ROWS):
  ratings = read_csv('ratings', READ_ROWS)

  movies_rating_list = {}

  with click.progressbar(ratings,
                         label='packing ratings:') as bars:
    for rating in bars:
      user_id = rating['userId']
      movies_rating_list.setdefault(user_id, {})
      movies_rating_list[user_id]['ratings.' +
                                  rating['movieId']] = float(rating['rating'])

  with click.progressbar(movies_rating_list.items(),
                         label='uploading user ratings:'
                         ) as bars:
    for user_id, rating_list in bars:
      ratings_db.push_new_rating_batch(str(ObjectId()), rating_list)


@click.group()
@click.option('--upload', is_flag=True)
def movie_admin(upload):
  click.echo(upload)


@movie_admin.command()
@click.option('--movies-list')
@click.argument('read-rows', default=-1, type=click.INT, required=False)
def movies_list(movies_list, read_rows):
  click.echo('uploading movies_list:%s' % read_rows)
  upload_movies_list(read_rows)


@movie_admin.command()
@click.option('--movies-rating')
@click.argument('read-rows', default=-1, type=click.INT, required=False)
def movies_rating(movies_rating, read_rows):
  click.echo('uploading raitngs:%s' % read_rows)
  upload_movies_rating(read_rows)


if __name__ == "__main__":
  movie_admin()
