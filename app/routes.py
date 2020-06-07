from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'user': 'Failix'}

    posts = [
        {
            'author': 'Asifa',
            'body': 'This was the best weekend ever!'
        },
        {
            'author': 'Iliyas',
            'body': 'Weekend brought blessings in disguise.'
        }
    ]

    return render_template('index.html', user=user, posts=posts)