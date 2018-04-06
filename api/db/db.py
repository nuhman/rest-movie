from api.db.firebase import database

class MovieDatabase():
  def get_movies(self, user):
    try:
      data = database.child('movies').get().val()
    except:
      data = {}
    return data

  def set_movies(self, movies_list):
      database.child('movies').set(movies_list)

class UserDatabase():
  def create_user(self, user):
    if(not self.get_user_by_google(user['googleId'])):
      data = database.child('users').push(user)
      data = {"id": data["name"]}
      data.update(user)
      return data
    return {};
  
  def get_user_by_google(self, googleId):
    data = database.child('users').order_by_child('googleId').equal_to(googleId).get() 
    if(data):
      for d in data.each():
        obj = {}
        obj.update(d.val())
        obj['id'] = d.key()
        return obj;
    return {}

  def get_user_by_id(self, id):
    data = database.child('users').child(id).get()
    data_with_id = {}
    if(data.val()):
      data_with_id.update({'id':data.key()})
      for d in data.each():
        data_with_id.update({d.key():d.val()})
    return data_with_id


if(__name__ == '__main__'):
  pass