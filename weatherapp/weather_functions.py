import requests
from datetime import *
import pytz
from config import Config

KEY = Config.KEY
cities = ['Mumbai', 'Pune', 'Nashik', 'Chennai', 'New Delhi', 'Amritsar', 'Agra', 'Surat']
forecast = 48

def get_city_weather(keyword):
    city_weather = []
    url = f'http://api.openweathermap.org/data/2.5/weather?q={keyword}&appid={KEY}&units=metric'
    response = requests.get(url)
    search_data = response.json()

    try:
        temperature = search_data['main']['temp']
        description = search_data['weather'][0]['description'].title()
        Feels_Like = search_data['main']['feels_like']
        Pressure = search_data['main']['pressure']
        Humidity = search_data['main']['humidity']
        Wind = search_data['wind']['speed']
        icon = search_data['weather'][0]['icon']
        city_weather.append((keyword, temperature, description, Feels_Like, Pressure, Humidity, Wind, icon))
    except KeyError:
        city_weather.append((keyword, 'N/A', 'N/A', 'N/A', 'N/A'))
    
    return city_weather




def get_daily_forecast(keyword):
    daily_forecast = []
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={keyword}&appid={KEY}&units=metric&cnt={forecast}'
    response = requests.get(url)
    daily_data = response.json()

    today = date.today()
    tomorrow = today + timedelta(days=1)

    try:
        for i in daily_data['list']:
            date_time = i['dt_txt']
            data_datetime = date_time.split()
            data_datetime1 = data_datetime[0]

            if data_datetime1 == today.strftime("%Y-%m-%d"):
                day = 'Today'
            elif data_datetime1 == tomorrow.strftime("%Y-%m-%d"):
                day = 'Tomorrow'
            else:
                day = data_datetime1

            time_1 = data_datetime[1]
            time_2 = datetime.strptime(time_1, "%H:%M:%S")
            time = time_2.strftime("%I:%M %p")

            weather_clouds = i['weather'][0]['main']
            weather_clouds_icon = i['weather'][0]['icon']
            temp_max = i['main']['temp_max']
            temp_min = i['main']['temp_min']
            pressur_e = i['main']['pressure']
            wind_speed = i['wind']['speed']



            sunrise_timestamp = daily_data['city']['sunrise']
            local_timezone = pytz.timezone('Asia/Tokyo')
            sunrise_datetime_utc = datetime.utcfromtimestamp(sunrise_timestamp)
            sunrise_datetime_local = sunrise_datetime_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
            sunrise = sunrise_datetime_local.strftime("%I:%M %p")
            
        
            sunset_timestamp = daily_data['city']['sunset']
            local_timezone = pytz.timezone('Asia/Kolkata')
            sunset_datetime_utc = datetime.utcfromtimestamp(sunset_timestamp)
            sunset_datetime_local = sunset_datetime_utc.replace(tzinfo=pytz.utc).astimezone(local_timezone)
            sunset = sunset_datetime_local.strftime('%I:%M %p')



            daily_forecast.append((day, time, weather_clouds, weather_clouds_icon, temp_max, temp_min, pressur_e, wind_speed, sunrise, sunset))
    except KeyError:
        pass
    return daily_forecast




def get_default_city_weather():
    default_city_weather = []
    for city in cities:
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric'
        response = requests.get(url)
        weather_data = response.json()

        try:
            temperature = weather_data['main']['temp']
            description = weather_data['weather'][0]['description'].title()
            default_city_weather.append((city, temperature, description))
        except KeyError:
            default_city_weather.append((city, 'N/A', 'N/A'))
    return default_city_weather
