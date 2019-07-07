"""
quickWeather.py - Prints the weather for a location from the command line.
A program from Automate the Boring Stuff
I reworked it so that it finds the weather from the location assigned to the
location variable.   The code for running the program from the command line is
commented out.   
"""

import json, requests, sys


"""
Compute location from command line arguments.  To use the command line 
take the take the triple quotes out around the if statemnt below and 
comment out the location variable assignment.
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])
"""

location = 'Valrico, US'
key = 'appid=8d195f72c65049d55c801a702f095e96'

#http://api.openweathermap.org/data/2.5/forecast?q=Valrico,us&appid=8d195f72c65049d55c801a702f095e96

# Download the JSON data from OpenWeatherMap.org's API.
url ='http://api.openweathermap.org/data/2.5/forecast/?q=%s&%s' % (location,key)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
print('Day after the day after tomorrow:')
print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after:')
print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
print()
print('Day after the day after tomorrow the day after the day after:')
print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])



print('\n\nweather data: \n', w)
print('\n\ntoday\'s weather data\n', w[0])
print('\n\ntoday\'s weather list\n', w[0]['weather'])
print()
print()
print(w[0]['weather'][0])
print()
print()
print(w[0]['weather'][0]['main'])