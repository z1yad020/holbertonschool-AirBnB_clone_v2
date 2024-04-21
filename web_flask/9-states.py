#!/usr/bin/python3

'''
task 9
'''

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """
    Rendern a template that displays a list of states.
    """
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def display_state_cities(id):
    """
    Render a template that displays a list of cities by state.
    """
    state = storage.all("State").values()
    val = None
    for s in state:
        if s.id == id:
            val = s

    return render_template("9-states.html", state=val)


@app.teardown_appcontext
def cl(random):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
