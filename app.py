import requests

class WeatherIntelligenceAgent:
    def __init__(self, api_key, location):
        self.api_key = api_key
        self.location = location
        self.api_url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather_data(self):
        params = {'q': self.location, 'appid': self.api_key}
        response = requests.get(self.api_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_weather(self):
        weather_data = self.get_weather_data()
        if weather_data:
            main = weather_data['main']
            weather = weather_data['weather'][0]
            print(f"Location: {self.location}")
            print(f"Temperature: {main['temp']} K")
            print(f"Weather: {weather['description']}")
        else:
            print('Weather data not available.')

if __name__ == '__main__':
    API_KEY = 'your_api_key_here'
    LOCATION = 'your_location_here'
    agent = WeatherIntelligenceAgent(API_KEY, LOCATION)
    agent.display_weather()