# pylint: disable=no-member, cyclic-import
# pylint doesn't recognize SQLAlchemy so we need to disable no-member
""" This is models.py, where each model for each table in the database is defined. """
from app import db

class User(db.Model):  # pylint: disable=too-few-public-methods
    """ This is the user model. The user model represents a user in the application. """
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        """ __repr__ defines what you see in the REPL when you interact with the
        database on the command line """
        return '<User {} {}, {}.>'.format(self.first_name, self.last_name, self.email)

    def __init__(self, first_name, last_name, email):
        """ this is what is required to create a new database object. if you do
        not include all of these things when trying to create a new user, you will
        receive an error and the new user will NOT be created. """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
