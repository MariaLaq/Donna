import os

import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.environ["OPENWEATHER_API_KEY"]

def get_weather(city, country_code):
    weather_json = requests.get(f"https://api.openweathermap.org/data/2.5/weather", params={"q": f"{city},{country_code}", "appid": api_key, "units": "imperial"})
    if weather_json.status_code != 200:
        print(f"Error: {weather_json.status_code}")
        return None
    else:
        weather_json = weather_json.json()
        weather_text = f"{weather_json['weather'][0]['description']}, {weather_json['main']['temp']}°F"


    return weather_text

if __name__ == "__main__":
    city = "New York"
    country_code = "US"
    weather = get_weather(city, country_code)
    print(weather)