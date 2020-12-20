from flask import json, jsonify, abort, request
from app import app
from app.models import Movie, Actor
from app.auth.auth import AuthError, get_token_auth_header, requires_auth, AUTH0_DOMAIN, CLIENT_ID, API_AUDIENCE, REDIRECT_URL, LOGOUT_URL
#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return 'Healthy'


@app.route('/logout')
def logout():
    return 'You are logged out'


# Define a route to get all Actors (/actors)
@app.route('/api/actors')
@requires_auth('get:actors')
def get_actors(payload):
    """This endpoint will retrieve all actors."""
    actors = Actor.query.all()

    return jsonify({
        'success': True,
        'actors': [actor.format() for actor in actors]
    }), 200


# Define a route to get all Movies (/movies)
@app.route('/api/movies')
@requires_auth('get:movies')
def get_movies(payload):
    """This endpoint will retrieve all movies."""
    movies = Movie.query.all()

    return jsonify({
        'success': True,
        'movies': [movie.format() for movie in movies]
    })


# Create a route to view an actor by ID
@app.route('/api/actors/<int:id>', methods=['GET'])
@requires_auth('get:actors')
def view_actor(payload, id):
    """This endpoint will show an actor by ID"""
    actor = Actor.query.get(id)

    return jsonify({
        'success': True,
        'actor': actor.format()
    })


# Create a route to view a movie by ID
@app.route('/api/movies/<int:id>', methods=['GET'])
@requires_auth('get:movies')
def view_movie(payload, id):
    """This endpoint will show a movie by ID"""
    movie = Movie.query.get(id)

    return jsonify({
        'success': True,
        'movie': movie.format()
    })


# Define a route to Create Actors (/actors)
@app.route('/api/actors', methods=['POST'])
@requires_auth('post:actor')
def create_actor(payload):
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


# define a route that can Patch actors by ID
@app.route('/api/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actor')
def update_actor(payload, id):
    """This endpoint will allow one to edit an actor"""
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


# Define a route that can Delete actors by ID
@app.route('/api/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actor')
def delete_actor(payload, id):
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
@requires_auth('post:movie')
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


# Genereate an Auth0 login session
@app.route("/authorization/url", methods=["GET"])
def generate_auth_url():
    """This endpoint will allow you to generate an auth URL"""
    url = f'https://{AUTH0_DOMAIN}/authorize' \
        f'?audience={API_AUDIENCE}' \
        f'&response_type=token&client_id=' \
        f'{CLIENT_ID}&redirect_uri=' \
        f'{REDIRECT_URL}'
    return jsonify({
        'url': url
    })


# Logout of Auth0
@app.route('/authorization/logout', methods=['GET'])
def generate_logout_url():
    """This endpoint will clear your Auth0 session."""
    url = f'https://{AUTH0_DOMAIN}/v2/logout?federated&' \
        f'client_id={CLIENT_ID}&returnTo={LOGOUT_URL}'

    return jsonify({
        'logout_url': url
    })


# Error Handlers
@ app.errorhandler(AuthError)
def process_AuthError(error):
    """AuthError effor handler."""
    response = jsonify(error.error)
    response.status_code = error.status_code

    return response
