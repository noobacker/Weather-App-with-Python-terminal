import requests

# Put your API key here     |    Dont forget to remove the quotes    |       Dont remove the single quotes
api_key = ' "YOUR_API_KEY" '

user_input = input("Enter city: ")

weather_data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}')

if weather_data.status_code != 200:
    print('City not found')
    exit()

weather = weather_data.json()['weather'][0]['main']
temp = round (weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")