import requests
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

API_KEY = os.getenv("API")

def API_call():
    r = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q=Prague&appid={API_KEY}&units=metric&lang=cz"
    )
    return r.json()

data = API_call()
print(data)
print("Město:", data["name"])
print("Teplota:", data["main"]["temp"], "°C")
print("Počasí:", data["weather"][0]["description"])
print("")
