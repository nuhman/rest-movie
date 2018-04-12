# REST API for movie-recommendation
## Overview

- ##### API
    - ##### db 
        - provide abstraction layer around CURD operation performed on the database
        - db.py
            - CURD operations
        - mongo.py
            - mongo setup files
    - ##### engine
        - core recommendation code
- app.py
  - entry point for the app 
- admin.py 
  - perform operations on the database directly


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
