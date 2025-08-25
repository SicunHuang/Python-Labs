"""
Takes a zip code as command line argument and prints out the temperature at this zip code location

CSCI 150 Lab 7

Name: Sicun Huang 
Section: A

Creativity:

"""
import urllib.request
import json
import sys

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "fe14277c654aaa8bca12785497cba138"

def get_temperature(zipcode):
    """
    use OpenWeatherMap API to get the current temperature at a location
    
    Args:
        zipcode: Zipcode for a location
    
    Return:
        Float value of temperature for that location
    """
    url = BASE_URL + 'zip=' + zipcode + ',us&APPID=' + API_KEY + "&units=imperial"
    with urllib.request.urlopen(url) as webpage:
        contents = webpage.read().decode('utf-8', 'ignore')
    d = json.loads(contents)
    temp = d['main']['temp']
    return float(temp)

def print_usage():
    """Print usage message for program"""
    print("usage: python3 lab7_weather.py <zipcode>")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()          
    else:
        zipcode = sys.argv[1]
        print(get_temperature(zipcode))



