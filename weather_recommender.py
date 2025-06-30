import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
api_key = (os.getenv("API_KEY"))

def get_weather(city):
    """
    Fetch weather data for a given city using the OpenWeatherMap API.

    Args:
        city (str): Name of the city to fetch weather for.

    Returns:
        list: A list containing:
            - [weather, weather_description] (list of str)
            - temperature (float, Kelvin)
            - wind_speed (float, m/s)

    Raises:
        ValueError: If the city is not found.
        requests.RequestException: If the API request fails.
    """
    # Get latitude and longitude for the city
    city_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}")
    city_reposnse_data = city_response.json()

    if not city_reposnse_data:
        raise ValueError("City not found.")

    lattitude = city_reposnse_data[0]["lat"]
    longitude = city_reposnse_data[0]["lon"]

    # Get weather data for the coordinates
    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&appid={api_key}")
    weather_response_data = weather_response.json()
    weather = weather_response_data["weather"][0]["main"]
    weather_description = weather_response_data["weather"][0]["description"]
    temperature = weather_response_data["main"]["temp"]
    wind_speed = weather_response_data["wind"]["speed"]

    return_list = [[weather, weather_description], temperature, wind_speed]

    return return_list
