# weatherapp\main_app\app.py

from flask import Flask, render_template, request
from weather_functions import get_city_weather, get_daily_forecast, get_default_city_weather
import pytz

app = Flask(__name__)

@app.route('/')
@app.route('/search', methods=['POST'])
def display_weather():
    default_city_weather = get_default_city_weather()
    city_weather = []
    daily_forecast = []


    if request.method == 'POST':
        keyword = request.form.get('keyword').title()
        if keyword:
            city_weather = get_city_weather(keyword)
            daily_forecast = get_daily_forecast(keyword)

    return render_template('weather.html', default_city_weather=default_city_weather, city_weather=city_weather, daily_forecast=daily_forecast)

if __name__ == '__main__':
    app.run(debug=False)
