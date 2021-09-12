
import requests
from config import API_KEY

def get_full_url(API_KEY):
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
    CITY = "riverside,"
    STATE_CODE = "california"
    UNIT = "imperial"

    URL = BASE_URL + CITY + "," + STATE_CODE + "&appid=" + API_KEY + "&units=" + UNIT
    return URL

def get_main_dict():
    URL = get_full_url(API_KEY)
    response = requests.get(URL)
    data = response.json() # data is in json format, need .json to read

    return data

def return_weather_results():
    data = get_main_dict()
    sub_1 = data['weather'][0]
    sub_2 = data['main']
    main = sub_1 | sub_2 #  merges two dictionaries

    d = dict()
    d['temperature'] = main['temp']
    d['humidity'] = main['humidity']
    d['pressure'] = main['pressure']
    d['weather_report'] = main['main']

    return d