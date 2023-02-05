#!/usr/bin/python3
"""
this script starts a Flask web application on the root
it displays “Hello HBNB!" and display some prompts
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function returns “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ This function returns “HBNB” """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
