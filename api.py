import requests

response = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=27&lon=-109&APPID=6f6dac66a608d477d024d9f0b59c3d59')
print(response.content)