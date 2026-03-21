import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Replace with your actual API key
API_KEY = 'YOUR_API_KEY'

@app.route('/weather/current/<city>', methods=['GET'])
def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/weather/forecast/<city>', methods=['GET'])
def get_weather_forecast(city):
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)