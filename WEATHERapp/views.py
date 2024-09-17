from django.shortcuts import render
import requests, datetime
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST['city']
    else:
        city='Kolhapur'
    WEATHER_API_KEY="d1e99fa4a624bc7d2ebc4b621d151a8d"
    weather_data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units_metric&APPID={WEATHER_API_KEY}")
    # print(weather_data.json())
    weather=weather_data.json()["weather"][0]['main']
    temp = round(weather_data.json()["main"]['temp'] -273.15)
    humidity=weather_data.json()["main"]['humidity']
    lon=weather_data.json()['coord']['lon']
    lat=weather_data.json()['coord']['lat']
    icon=weather_data.json()['weather'][0]['icon']
    day=  datetime.date.today()
    
    weather=weather_data.json()["weather"][0]
    main=weather['main']
    description=weather['description']
    return render(request,'index.html',{'city': city, 'description': description, 'main': main, 'temp': temp, 'humidity': humidity, 'lon':lon, 'lat':lat, 'day':day, 'icon': icon} )