import pyowm
import time

owm = pyowm.OWM('API Key for OpenWeather here')

observation = owm.weather_at_place('location')
w = observation.get_weather()
#print(w)
n = 0
fc = owm.daily_forecast('location', limit=5)
f = fc.get_forecast()

fc2 = owm.three_hours_forecast('location')
f2 = fc2.get_forecast()

wind = w.get_wind()
humidity = w.get_humidity()
temp = w.get_temperature('fahrenheit')
clouds = w.get_clouds()
rain = w.get_rain()
snow = w.get_snow()
stat = w.get_status()
srise = w.get_sunrise_time()
sset = w.get_sunset_time()


print ('Sunrise at: ' + time.ctime(srise))
print ('Sunset at: ' + time.ctime(sset))
print (temp)
print ('Humidity: ' + str(humidity) + '%')
print ('Current Status: ' + stat)
print ('Cloud coverage: ' + str(clouds) + '%')
print ('wind: ' + str(wind))
print ('Rain volume: ' + str(rain))
print ('Snow volume: ' + str(snow))

print('\n''Five day forecast')
for weather in f:
    print(time.ctime(weather.get_reference_time()),weather.get_status())

print('\n''Three hour forcast')
for weather in f2:
    print(time.ctime(weather.get_reference_time()),weather.get_status())

input('\n''Press any key to exit')
