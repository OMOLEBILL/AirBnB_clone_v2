#!/usr/bin/python3
"""This shows the lists of sates in a database"""

from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(exception=None):
    """ This fuctions remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_state():
    """list all the states"""
    states = list(storage.all('State').values())
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
