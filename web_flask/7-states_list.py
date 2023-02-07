#!/usr/bin/python3
"""This shows the lists of sates in a database"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception=None):
    """ This fuctions remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_state():
    """list all the states"""
    states = list(storage.all('State').values())
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
