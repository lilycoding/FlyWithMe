""" This is routes.py, where we determine what will be delivered to the frontend. """
# pylint: disable=cyclic-import
from flask import render_template
from app import app
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    """ This is the most basic API call, and returns some basic user information to
    templates/index.html. Below, we get the first user from the database and return
    it in the user dictionary to deliver to the user on the front end in
    templates/index.html. """
    user = User.query.first()
    return render_template(
        'index.html',
        title='Fly With Me!',
        user={
                'first_name': user.first_name,
                'last_name': user.last_name
            })
