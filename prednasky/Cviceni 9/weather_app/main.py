# pylint: disable=missing-module-docstring, missing-function-docstring, no-name-in-module, import-error

from fastapi import FastAPI
from geocoding_api import get_coordinates_current_location
from weather_api import get_weather, get_weather_for_city

app = FastAPI()


@app.get("/")
def get_root():
    return {"message": "OK"}


@app.get("/weather")
def get_all():
    weather_data = get_weather(*get_coordinates_current_location())
    return weather_data["current"]


@app.get("/weather/{city}")
def get_all_city(city: str):
    weather_data = get_weather_for_city(city)
    weather_data = weather_data["current"]
    weather_data.update({"city": city})
    return weather_data


@app.get("/temperature")
def get_temp():
    weather_data = get_weather(*get_coordinates_current_location())
    return {
        "temp": weather_data["current"]["temp"],
        "sunrise": weather_data["current"]["sunrise"],
        "sunset": weather_data["current"]["sunset"],
    }


@app.get("/temperature/{city}")
def get_temp_for_city(city: str):
    weather_data = get_weather_for_city(city)
    return {
        "city": city,
        "temp": weather_data["current"]["temp"],
        "sunrise": weather_data["current"]["sunrise"],
        "sunset": weather_data["current"]["sunset"],
    }