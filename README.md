# weather-app
This is a weather app created in python. Gives output in console

## API

The api link - https://weatheraapi.com/
Price - 0$ for 1000000 use per month

Sign in take the key and paste it in the code where the 



## json
```json
{
    "location": {
        "name": "Bihar",
        "region": "Bihar",
        "country": "India",
        "lat": 25.18,
        "lon": 85.52,
        "tz_id": "Asia/Kolkata",
        "localtime_epoch": 1640861078,
        "localtime": "2021-12-30 16:14"
    },
    "current": {
        "last_updated_epoch": 1640860200,
        "last_updated": "2021-12-30 16:00",
        "temp_c": 22.0,
        "temp_f": 71.6,
        "is_day": 1,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
            "code": 1003
        },
        "wind_mph": 4.7,
        "wind_kph": 7.6,
        "wind_degree": 330,
        "wind_dir": "NNW",
        "pressure_mb": 1019.0,
        "pressure_in": 30.09,
        "precip_mm": 0.0,
        "precip_in": 0.0,
        "humidity": 58,
        "cloud": 36,
        "feelslike_c": 24.6,
        "feelslike_f": 76.3,
        "vis_km": 10.0,
        "vis_miles": 6.0,
        "uv": 6.0,
        "gust_mph": 5.6,
        "gust_kph": 9.0,
        "air_quality": {
            "co": 767.7000122070312,
            "no2": 7.699999809265137,
            "o3": 98.69999694824219,
            "so2": 9.899999618530273,
            "pm2_5": 69.69999694824219,
            "pm10": 78.30000305175781,
            "us-epa-index": 4,
            "gb-defra-index": 9
        }
    }
}
```

## Code

### importing 
```py
import requests
import os
```
```py
### requesting api
my_secret = os.environ['Api']
response= requests.get(my_secret)
data = response.json()
```
### finishing
```py
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
```
## Output 
```console
Time
Place 
Country
Humidity
```



