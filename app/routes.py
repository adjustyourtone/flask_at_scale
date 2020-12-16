from flask import jsonify, abort, request, redirect
from app import app
from app.models import Movie, Actor

#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return 'Healthy'


# Define a route to get Actors (/actors)
@app.route('/actor')
def get_actors():
    pass


# Define a route to get Movies (/movies)
@app.route('/movies')
def get_movies():
    pass


# Define a route to Create Actors (/actors)
@app.route('/actors', methods=['POST'])
def create_actor():
    pass


# define a route that can Patch and Delete actor by ID
@app.route('/actors/<int:id>', methods=['PATCH', 'DELETE'])
def update_actors(id):
    pass


# Define a route to Create Movies (/movies)
@app.route('/movies', methods=['POST'])
def create_movies():
    pass


# Define a route to Patch and Update movies by ID
@app.route('/movies/<int:id>', methods=['PATCH', 'DELETE'])
def update_movies(id):
    pass
