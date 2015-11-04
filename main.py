"""`main` is the top level module for your Flask application."""

# Import the Flask Framework
from flask import Flask, jsonify
import random
app = Flask(__name__)
# Note: We don't need to call run() since our application is embedded within
# the App Engine WSGI application server.


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    list =  ["http://i.imgur.com/1CzMDjg.jpg",
    "http://i.imgur.com/qaghMWe.jpg",
    "http://i.imgur.com/VP0qn6T.jpg",
    "http://i.imgur.com/eQQbcxe.jpg",
    "http://i.imgur.com/kd4iDTh.jpg",
    "http://i.imgur.com/X89iRAN.jpg",
    "http://i.imgur.com/w2GWoJu.jpg",
    "http://i.imgur.com/kSzF0Dh.jpg",
    "http://i.imgur.com/lCDLHU1.jpg"]
    sub_list = random.sample(list, 10)
    return jsonify(results=sub_list)


@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, Nothing at this URL.', 404


@app.errorhandler(500)
def application_error(e):
    """Return a custom 500 error."""
    return 'Sorry, unexpected error: {}'.format(e), 500
