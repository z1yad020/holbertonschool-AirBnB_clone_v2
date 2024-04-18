#!/usr/bin/python3

'''
task 3
'''

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    return f'C {escape(text).replace("_", " ")}'


@app.route("/python", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_is_fun(text):
    return f'Python {escape(text).replace("_", " ")}'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)
