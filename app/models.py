from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    first_name = db.Column(db.String(64), index=True, unique=True)
    last_name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        # this is what you see when you interact with the db in the repl/terminal
        return '<User {} {}, {}.>'.format(self.first_name, self.last_name, self.email)

    def __init__(self, first_name, last_name, email):
        # this is what is required to create a new database object
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
