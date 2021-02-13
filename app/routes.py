from flask import render_template
from app import app
from app.models import User

@app.route('/')
@app.route('/index')
def index():
    user = User.query.first()
    return render_template(
        'index.html', 
        title='Fly With Me!', 
        user={
                'first_name': user.first_name,
                'last_name': user.last_name
            })
