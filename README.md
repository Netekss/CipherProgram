# Cipher Project
## Cipher Python app

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Todo](#todo)

## General info
This app base on Caesar cipher, but it's more complex. This cipher isn't changing value
for each letter once, but couple time. Key is different for values placed on even and odd index.
The returned string is reversed, and the order of the letters has been changed. Key with tips how
to decode also has benn changed couple time.



## Technologies
Project is created with:
* Python 3.8
* FastAPI
* Hypercorn

## Setup
Step 1:
* virtualenv venv
* venv/bin/activate

Step 2:\
pip install -r requirements.txt

Step 3:\
Type in terminal: hypercorn server:app --reload

Step 4:\
Go to http://127.0.0.1:8000/docs

Login and Password:\
login = admin\
password = superuser\
If you want, you can change login or password in server.py


## Todo
* Repair bug which sometimes appear in FastAPI while decoding
    - {"detail":"Not Found"} when "/" in string\
      At this moment, removed "/" from available characters