#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index1():
    """displays the string Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index2():
    """displays the string HBNB!"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def index3(text):
    """Displays C followed by what's in text"""
    newtext = text.replace('_', ' ')
    return 'C ' + newtext


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
