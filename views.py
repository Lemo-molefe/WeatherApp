from django.shortcuts import render

import requests
from django.shortcuts import render

def index(request):
    weather_data = None  # Default value
    if 'city' in request.GET:
        city = request.GET['city']  # Get city name from the form
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=95c914da316550bcc864887abb795a07&units=metric"

        response = requests.get(api_url)
        if response.status_code == 200:
            weather_data = response.json()

    return render(request, 'weather/index.html', {'weather_data': weather_data})

