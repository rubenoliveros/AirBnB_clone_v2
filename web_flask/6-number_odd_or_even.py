#!/usr/bin/python3
"""
A script that starts a Flask web application
"""

from flask import Flask
from flask import render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def index4(text='is cool'):
    """Displays Python followed by what's in text"""
    newtext = text.replace('_', ' ')
    return 'Python ' + newtext


@app.route('/number/<int:number>', strict_slashes=False)
def index5(number):
    """Displays the argument if number is an integer"""
    return '%d is a number' % number


@app.route('/number_template/<int:number>', strict_slashes=False)
def index6(number):
    """Display a HTML page if number is an integer"""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>', strict_slashes=False)
def index7(number):
    """Display a HTML page if number is even or odd"""
    if number % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'
    return render_template('6-number_odd_or_even.html', number=number,
                           even_or_odd=even_or_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
