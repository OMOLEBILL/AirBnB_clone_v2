#!/usr/bin/python3
"""
this script starts a Flask web application on the root
it displays “Hello HBNB!"
"""
from flask import Flask, escape
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
def c_text(text):
    """display “C ” followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"C {escape(text)}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
