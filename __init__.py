import flask
import GameFetcher
from GameFetcher import GamesDAO
from flask import request, jsonify
from flask_cors import CORS

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

@app.route('/api/v1/', methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p>This site is a prototype API for distant reading of science fiction novels.</p>"

@app.route('/api/v1/games', methods=['GET'])
def games():
    games = GamesDAO.getMovies()
    return games

@app.route('/api/v1/games/search', methods=['GET'])
def getGame():
    if 'word' in request.args:
        search_word = request.args['word']
        games = GamesDAO.getMovie(search_word)
        return games
    else:
        return "Error: No search parameter was given."

app.run()
