# weatherapp\tests\test_weather_functions.py
import unittest
from weather_functions import get_city_weather
from config import Config

class TestApp(unittest.TestCase):
    def test_get_city_weather(self):

        key = Config.KEY
        keyword = 'Mumbai'

        response = get_city_weather(keyword)

        self.assertEqual(response.status_code, 200)            

if __name__ == '__main__':
    unittest.main()