"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, jsonify
import random
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.

def create_pool():
    mylist = []
    with open("images-urls.txt") as f:
        for line in f:
            line = line.strip()
            if line != "":
                mylist.append(line)
    return mylist


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    mylist = create_pool()
    sub_list = random.sample(mylist, 50)
    return jsonify(results=sub_list)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
