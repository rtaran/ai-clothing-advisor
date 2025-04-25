import requests
import os
from dotenv import load_dotenv
from openai import OpenAI
# from data import insert_weather_dat
load_dotenv()
API_KEY = os.getenv("API_GEO_KEY")
API_OPENAI_KEY = os.getenv("API_OPENAI_KEY")

client = OpenAI(api_key=API_OPENAI_KEY)

class WeatherApp:

    def __init__(self, city, country):
        self.longitude = None
        self.latitude = None
        self.temperatur = None
        self.windspeed = None
        self.city = city
        self.country = country

    def get_coordinates(self):
        url = f"https://api.api-ninjas.com/v1/geocoding?city={self.city}&country={self.country}" # API for geoposition: lat and long
        headers = {'X-Api-Key': API_KEY}
        response = requests.get(url, headers)

        if response.status_code == 200:
            geo_data = response.json()
            if not geo_data:
                print("API works, but no location found.")
            self.longitude = geo_data[0]["latitude"]
            self.latitude = geo_data[0]["latitude"]
        else: print(f"Error fetching data, the status code is:{response.status_code}")

    def get_weather(self):
        url = "https://api.open-meteo.com/v1/forecast"

        parameters = {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "current_weather": True
        }
        response = requests.get(url, params=parameters)

        if response.status_code == 200:
            weather_data = response.json()
            self.temperatur = int(weather_data["current_weather"]["temperature"])
            self.windspeed = int(weather_data["current_weather"]["windspeed"])
        else: print(f"Error fetching data, the status code is:{response.status_code}")

    def suggest_clothing(self):
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": 'system', "content": "You are a helpfull weather stylist assistant with sense of humor."},
                {"role": "user",
                 "content": f"for {self.city} with {self.temperatur} degrees and {self.windspeed} kmh, "
                            f"suggest me some clothes to wear"}
            ]
        )
        print(response.choices[0].message.content)

    def get_weekly_forecast(self):
        pass






