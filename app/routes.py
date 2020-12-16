from flask import jsonify, abort, request, redirect
from app import app
# from app.models import Student, Teacher, Lesson

#----------------------------------------------------------------------------#
# Routes
#----------------------------------------------------------------------------#


@app.route('/')
def index():
    return 'Healthy'