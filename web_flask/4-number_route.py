#!/usr/bin/python3

""" Simple Flask App """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ returns Hello HBNB! """

    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns HBNB """

    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text=None):
    """ returns C followed by text """

    return f'C {text.replace("_", " ")}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """ returns Python followed by text """

    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ returns n is a number """

    return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
