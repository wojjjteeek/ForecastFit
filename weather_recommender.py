import requests
import json
import os
from dotenv import load_dotenv, dotenv_values 

load_dotenv()
api_key = (os.getenv("API_KEY"))

def get_weather(city):
    city_response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}")
    city_reposnse_data = city_response.json()

    lattitude = city_reposnse_data[0]["lat"]
    longitude = city_reposnse_data[0]["lon"]

    weather_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lattitude}&lon={longitude}&appid={api_key}")
    weather_response_data = weather_response.json()
    weather = weather_response_data["weather"][0]["main"]
    weather_description = weather_response_data["weather"][0]["description"]
    temperature = weather_response_data["main"]["temp"]
    celsius = temperature - 273.15
    fahrenheit = (temperature - 273.15) * 9/5 + 32
    wind_speed = weather_response_data["wind"]["speed"]
    if wind_speed <= 3:
        wind_speed_category = "Small or No Wind"
    elif wind_speed <= 7:
        wind_speed_category = "Pretty Windy"
    elif wind_speed <= 13:
        wind_speed_category = "Very Windy"
    else:
        wind_speed_category = "Hurricane"

    return_list = [[weather, weather_description], temperature, wind_speed]

    return return_list
