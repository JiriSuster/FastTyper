# pylint: disable=missing-module-docstring, missing-function-docstring, no-name-in-module, import-error
from typing import Tuple

import requests
from geopy.geocoders import Nominatim


class PlaceNotFound(Exception):
    """ Exception for place not found. """


def get_coordinates_for_place(place_name: str) -> Tuple[str]:
    geolocator = Nominatim(user_agent="mendelu_python_course")
    location = geolocator.geocode(place_name)
    if location:
        return location.latitude, location.longitude
    raise PlaceNotFound(f"Location {place_name} not found")


def get_coordinates_current_location() -> Tuple[str]:
    req = requests.get("http://ip-api.com/json", timeout=10)
    return req.json()["lat"], req.json()["lon"]