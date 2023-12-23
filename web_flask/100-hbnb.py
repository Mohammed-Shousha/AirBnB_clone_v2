#!/usr/bin/python3

""" Simple Flask App """

from flask import Flask, render_template, Markup
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def states_cities_list():
    """display a HTML page like 8-index.html from static"""
    states = list(storage.all("State").values())
    states.sort(key=lambda x: x.name)
    for state in states:
        state.cities.sort(key=lambda x: x.name)
    amenities = list(storage.all("Amenity").values())
    amenities.sort(key=lambda x: x.name)
    places = list(storage.all("Place").values())
    places.sort(key=lambda x: x.name)
    for place in places:
        place.description = Markup(place.description)
    return render_template(
        '100-hbnb.html',
        states=states,
        amenities=amenities,
        places=places
    )


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
