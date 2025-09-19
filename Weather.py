import requests

API_KEY = 'API'
City_name = input("Enter City name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={API_KEY}&units=metric'

response = requests.get(url)

if response.status_code == 200:
    weather_data = response.json()
    temp = weather_data['main']['temp']
    description = weather_data['weather'][0]['description']
    city = weather_data['name']
    print(f"Weather in {city}: {description}, Temperature: {temp}°C")
else:
    print(f"Error {response.status_code}: {response.json().get('message', 'Unknown error')}")
