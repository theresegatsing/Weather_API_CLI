'''
Author: Therese Elvira Mombou Gatsing
'''
import requests

#All the requeets are made to the Base URL
Base_URL = "https://api.openweathermap.org/data/2.5/weather"

#API key to know which user is making the request
API_Key ="dc9c2f1ddf70453550bc3aa7f7b37f57"

def get_weather(city):
    response = requests.get(Base_URL,
                            params ={"q":city,
                                     "appid":API_Key,
                                     "units":"metric" }
                            )#get the temperatur in celsius

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}: {data['weather'][0]['description'].title()}")
        print(f"Humidity:{data['main']['humidity']}%")
        print(f"Temperature:{data['main']['temp']}°C")
    else:
        print("City not found or API error")

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
    
                            
                
                            
