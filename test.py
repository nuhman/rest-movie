from dotenv import load_dotenv
load_dotenv(verbose=True)

from api.db.rating_database import RatingDatabase

r_db = RatingDatabase()


r_db.get_all_rating()
