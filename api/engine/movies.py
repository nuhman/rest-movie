from api.db.movie_database import MovieDatabase

movie_db = MovieDatabase()


def get_movies(user):
  return movie_db.get_movies()
