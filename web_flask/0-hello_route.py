#!/usr/bin/python3
"""
this script starts a Flask web application on the root
it displays “Hello HBNB!"
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """This function returns “Hello HBNB!”"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
