# REST API for movie-recommendation
## Overview

- #### API
    - #### config
    - #### db provide abstraction layer around CURD operation performed on the database
    - #### engine core recommendation code
- app.py  entry point for the app 
- admin.py  perform operations on the database directly


## Setup 
### Install and setup virutalenv 

- ` pip install virtaulenv `
- ` virtualenv flask_env `

### Activate virtaul environment/Intial Setup

- `flask_env\Scripts\Activate`
- `pip install -r requirements.txt`

### Run app 

- `flask_env\Scripts\Activate`
- `SET FLASK_APP=app.py`
- `flask run --with-threads`


## Usage

### Admin 

#### Uploading movies list to database 

```
python admin.py --upload movies_list [NO_OF_ROWS_TO_UPLOAD]
```

#### Uploading movies rating to database 

```
python admin.py --upload movies_rating [NO_OF_ROWS_TO_UPLOAD]
```
 
### REST API
### Get movie list from the database:

```
GET: http://localhost:5000/movies/list/22142

Response: 
[
    {
        "genres": [
            "Adventure",
            "Animation",
            "Children",
            "Comedy",
            "Fantasy"
        ],
        "id": "5aceeeb235a49d14cc0679d8",
        "image": "http://url/file.png",
        "imdbId": "0114709",
        "movieId": "1",
        "title": "Toy Story (1995)",
        "tmdbId": "862"
    },
 ]
```

### Create new user 
```
POST: http://localhost:5000/users/create
JSON-payload: 
{
  "googleId": "$googleId",
  "thumbnail" : "$user_profile_image_url",
  "username": "$username"
}

Response:
{
  "googleId": "$googleId",
  "id": "$objectId",
  "thumbnail": "$user_profile_image_url",
  "username": "$username"
}

```

### Get user by google-id
```
POST: http://localhost:5000/users/get-google
JSON-payload:
{  
  "googleId": "$googleId"
}

Response:
{
  "googleId": "$googleId",
  "id": "$objectId",
  "thumbnail": "$user_profile_image_url",
  "username": "$username"
}
'''
### Get user by user-id 
'''
POST: http://localhost:5000/users/get-id
JSON-payload:
{
  "id": "$objectId"
}

Response:
{
  "googleId": "$googleId",
  "id": "$objectId",
  "thumbnail": "$user_profile_image_url",
  "username": "$username"
}
```


## other resources

 [click documentation](http://click.pocoo.org/5/)
