import requests


city = input("Enter the name of city: ")
api_key = "07f74d20ca3e60e791f6eca11cdcc317"

def get_weather(api_key, city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url).json()
    temp = response['main']['temp']
    temp_to_cel = temp-273.15  # convert kelvin to celsius
    print(f"The temperature in {city} is {int(temp_to_cel)}℃")

get_weather(api_key, city)