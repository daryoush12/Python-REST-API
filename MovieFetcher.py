import pymongo
from pymongo import MongoClient
import json
from bson import Binary, Code
from bson.json_util import dumps
with open('./settings.json') as settings_json:
    settings = json.load(settings_json)
    client = MongoClient(settings['mongo_uri'])

    
class GamesDAO:

    global settings
    global client

    def getMovies(self):
        db = client.MoviesBase
        movies = dumps(db.Movies.find({}))
        return movies

    def getMovie(self, search_word):
        db = client.MoviesBase
        movie = dumps(db.Movies.find_one(search_word))
        return movie

    

    

