"""
quickWeather.py - Prints the weather for a location from the command line.
This program is similar to a program found in the online textbook "Automate the Boring Stuff."
It uses api from openweathermap.org.  Since the writing of the textbook the site now requires keys. The keys for forecast data are free once you register with the website.  I reworked the code for the url to use the key I was given by the service.  I also changed the program so that it finds the weather from the location assigned to the location variable.   The code for running the program from the command line is commented out but can be easily put back in.
   
Ambrioso (Summer 2019)
"""
# These are the libraries used by the program.
import json, requests, sys

"""
Links to the documentation for these important libraries and the home of JSON.
https://docs.python.org/3/library/json.html
http://json.org/
https://docs.python.org/3/library/sys.html
https://pypi.org/project/requests/
""”

“””
Some things to do:
(1). Review format of JSON data.
(2). Review indexing by print out other parts of the data.
(3). Write a temperature conversion function and using it with the data.
F = (9/5)*(K - 273) + 32
(4). Compute the average of the temperature data.
“””

"""
Compute location from command line arguments.  To use the command line 
take the take the triple quotes out around the if statement below and 
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
print('The day after tomorrow:')
print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])
print()
print('The day after the day after tomorrow:')
print(w[3]['weather'][0]['main'], '-', w[3]['weather'][0]['description'])
print()
print('The day after the day after the day after tomorrow:')
print(w[4]['weather'][0]['main'], '-', w[4]['weather'][0]['description'])
print()
print('The day after the day after the day after the day after tomorrow:')
print(w[5]['weather'][0]['main'], '-', w[5]['weather'][0]['description'])



print('\n\nWeather data w: \n', w)
('\nToday\'s weather data w[0]:\n', w[0])
print('\nToday\'s weather list w[0][\'weather\']:\n', w[0]['weather'])
print('\nFirst item in weather list:\n', w[0]['weather'][0])
print('\nToday\'s weather w[0][\'weather\'][0][\'main\']:\n', w[0]['weather'][0]['main'])
