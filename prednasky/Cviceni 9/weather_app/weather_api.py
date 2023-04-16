# pylint: disable=missing-module-docstring, missing-function-docstring, no-name-in-module, import-error
from typing import Dict

import requests

APP_ID = "2efe7500fec496570d121d95590467cf"


class WeatherAPIError(Exception):
    "Weather API error"


class GeocodingAPIError(Exception):
    """ Geocoding API error """


def get_weather(lat: float, lon: float) -> Dict[str, str]:
    request_data = {"lat": lat, "lon": lon, "appid": APP_ID, "units": "metric"}
    req = requests.get(
        "https://api.openweathermap.org/data/2.5/onecall", params=request_data, timeout=10
    )
    if req.status_code == 200:
        return req.json()
    raise WeatherAPIError()


def get_weather_for_city(city: str) -> Dict[str, dict]:

    req = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={APP_ID}", timeout=10
    )
    if req.status_code == 200:
        geoinfo = req.json()[0]  # limit 1
        return get_weather(geoinfo["lat"], geoinfo["lon"])
    raise GeocodingAPIError()