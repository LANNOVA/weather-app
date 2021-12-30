import requests
import os

response= requests.get(api key)
data = response.json()
                       #print(response.json())
print(response.json())
from datetime import datetime

e = data['location']
f = e['name']
g = data['current']
h = g['condition']
country = e['country']
print(e['localtime'])
print(f)
print(country)
temp = g['temp_c']
print(temp)
humid = g["humidity"]
print(humid)


