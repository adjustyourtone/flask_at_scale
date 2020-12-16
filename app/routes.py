from flask import json, jsonify, abort, request, redirect
from app import app
from app.models import Movie, Actor

#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return 'Healthy'


# Define a route to get all Actors (/actors)
@app.route('/api/actors')
def get_actors():
    """This endpoint will retrieve all actors."""
    actors = Actor.query.all()

    return jsonify({
        'success': True,
        'actors': [actor.format() for actor in actors]
    })


# Define a route to get all Movies (/movies)
@app.route('/api/movies')
def get_movies():
    """This endpoint will retrieve all movies."""
    movies = Movie.query.all()

    return jsonify({
        'success': True,
        'movies': [movie.format() for movie in movies]
    })


# Create a route to view an actor by ID
@app.route('/api/actors/<int:id>', methods=['GET'])
def view_actor(id):
    """This endpoint will show an actor by ID"""
    actor = Actor.query.get(id)

    return jsonify({
        'success': True,
        'actor': actor.format()
    })


# Create a route to view a movie by ID
@app.route('/api/movies/<int:id>', methods=['GET'])
def view_movie(id):
    """This endpoint will show a movie by ID"""
    movie = Movie.query.get(id)

    return jsonify({
        'success': True,
        'movie': movie.format()
    })


# Define a route to Create Actors (/actors)
@app.route('/api/actors', methods=['POST'])
def create_actor():
    """This endpoint will allow the creation of a new actor."""
    data = request.get_json()

    try:
        new_actor = Actor()
        new_actor.name = data['name']
        new_actor.age = data['age']
        new_actor.gender = data['gender']

        new_actor.insert()

    except:
        abort(400)

    return jsonify({
        'success': True,
        'actor': new_actor.format()
    }), 200


# define a route that can Patch and Delete actors by ID
@app.route('/api/actors/<int:id>', methods=['PATCH', 'DELETE'])
def update_actor(id):
    """This endpoint will allow one to edit or delete an actor"""
    if request.method == 'PATCH':

        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        data = request.get_json()

        if 'name' in data:
            actor.name = data['name']

        if 'age' in data:
            actor.age = data['age']

        if 'gender' in data:
            actor.gender = data['gender']

        actor.update()

        return jsonify({
            'success': True,
            'actor': actor.format()
        }), 200

    if request.method == 'DELETE':
        actor = Actor.query.get(id)

        if actor is None:
            abort(404)

        actor.delete()

        return jsonify({
            'success': True,
            'delete': actor.format()
        }), 200


# Define a route to Create Movies (/movies)
@app.route('/api/movies', methods=['POST'])
def create_movies():
    """This endpoint will allow the creation of a new movie."""
    data = request.get_json()

    try:
        new_movie = Movie()
        new_movie.title = data['title']
        new_movie.release_date = data['release_date']

        new_movie.insert()

    except:
        abort(400)

    return jsonify({
        'success': True,
        "movie": new_movie.format()
    }), 200


# Define a route to Patch and Update movies by ID
@app.route('/api/movies/<int:id>', methods=['PATCH', 'DELETE'])
def update_movies(id):
    """This endpoint will allow one to edit or delete a movie."""
    if request.method == 'PATCH':
        movie = Movie.query.get(id)

        if movie is None:
            abort(404)

        data = request.get_json()

        if 'title' in data:
            movie.title = data['title']

        if 'release_date' in data:
            movie.release_date = data['release_date']

        movie.update()

        return jsonify({
            'success': True,
            'movie': movie.format()
        }), 200

    if request.method == 'DELETE':
        movie = Movie.query.get(id)

        movie.delete()

        return jsonify({
            'success': True,
            'deleted': movie.format()
        }), 200
