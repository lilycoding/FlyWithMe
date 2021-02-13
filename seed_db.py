from app.models import User
from app import db

users = User.query.all()
users_length = len(users)

if users_length == 0:
    alice = User(first_name='Alice', last_name='Wonderland',  email='student@example.com')
    db.session.add(alice)
    db.session.commit()
