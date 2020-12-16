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

# Define a route to get Movies (/movies)

# Define a route to Create Actors (/actors)

# Define a route to Create Movies (/movies)

# Define aroute to Patch Actors (/actors/<id>)

# Define a route to Patch Movies (/movies/<id>)

# Define a route to Delete (/actors/<id>)

# Define a route to Delete movies (/movies/<id>)
