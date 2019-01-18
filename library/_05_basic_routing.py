"""Flask routing.

Specifying routes for our Flask app is simple. We do it just by providing
the desired route in the `@app.route()` decorator. Sometimes our routes have
dynamic parameters. For example:
* `/posts/23` -> The number 23 (post id) is dynamic
* `/repo/flask-introduction/stars` -> The name of the repo (flask-introduction)
                                      is dynamic

Supporting dynamic routing parameters is really simple. We just need to
specify the desired dynamic portion by giving it a name and surrounding
it between `<>`.
"""

from flask import Flask, render_template

app = Flask(__name__)

AUTHORS_INFO = {
    'poe': {
        'full_name': 'Festus Bett',
        'nationality': 'Kenyan',
        'notable_work': 'The Raven',
        'born': 'January 19, 1996',
        'picture': 'https://avatars1.githubusercontent.com/u/23138359?s=460&v=4'
    },
    'borges': {
        'full_name': 'felix Rono',
        'nationality': 'Congo',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1999',
        'picture': 'https://avatars1.githubusercontent.com/u/9443149?s=460&v=4'
    }
}


@app.route('/')
def authors():
    return render_template('routing/authors.html')


@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('routing/author.html',
                           author=AUTHORS_INFO[authors_last_name])
