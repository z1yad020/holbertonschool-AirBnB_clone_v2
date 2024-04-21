#!/usr/bin/python3
"""
task 10
"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """all state and amen."""
    states = sorted(storage.all("State").values(), key=lambda x: x.name)
    amenities = sorted(storage.all("Amenity").values(), key=lambda x: x.name)

    for state in states:
        state.cities = sorted(state.cities, key=lambda x: x.name)

    return render_template(
        "10-hbnb_filters.html",
        states=states,
        amenities=amenities,
    )


@app.teardown_appcontext
def teardown(exc):
    """Remove session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
