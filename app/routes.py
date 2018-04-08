from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Kevin'}
    posts = [
        {
            'author': 'Kevin',
            'body': 'I am learning to use Flask'
        },
        {
            'author': 'Kevin',
            'body': 'I hope to make my own personal website'
        },
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
