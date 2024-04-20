#!/usr/bin/python3

'''
task 7
'''

from models import storage
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    states = storage.all("State").values()
    sorted_states = sorted(states, key=lambda x: x.name)
    return render_template("7-states_list.html", states=sorted_states)


@app.teardown_appcontext
def cl(random):
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
