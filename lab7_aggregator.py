"""
appends the temperature for current date and hour in a location (if not already exists) to a file 

CSCI 150 Lab 7

Name: Sicun Huang 
Section: A

Creativity:

"""
import datetime
import sys
import os
import lab7_weather

   
def get_hour():
    """get the current hour"""
    now = datetime.datetime.now()
    return str(now.hour)
   
def get_date():
    """get the current date in month-day-year format"""
    now = datetime.datetime.now()
    return str(now.month) + "-" + str(now.day) + "-" + str(now.year)

def get_date_time():
    """get the current date and hour in a single string"""
    return get_date() + "," + get_hour()
             
def add_entry(zipcode):
    """
    generate an entry of temperature in current date and time
    
    Args:
        zipcode: Zipcode of the location
    
    Return:
        an entry in the format of day-month-year,hour,temperature
    """    
    return get_date_time() + "," + str(lab7_weather.get_temperature(zipcode))  # zipcode as a string

def write_to_file(filename,zipcode):
    """
    append the entry of temperature to a file
    
    Args：
        filename: Name of the file to which entry is appended
        zipcode: Zipcode of the location
    
    Return:
        an entry with newline at the end
    """
    with open(filename, 'a') as file:
        file.write(add_entry(zipcode) + "\n")

def print_usage():
    """Print usage message for program"""
    print("usage: python3 lab7_aggregator.py <file> <zip_code>")
    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print_usage()          
    else:
        filename = sys.argv[1]
        zipcode = sys.argv[2]
        if os.path.exists(filename) == True: #file exists
            result = ""
            with open(filename, 'r') as file:
                for line in file:
                    result += line + ','
            if get_date_time() not in result:
                # only add entry when current date and time isn't in the file already
                write_to_file(filename,zipcode)
        else: #file doesn't exist
            write_to_file(filename,zipcode)


                   
            
                   
            
            
            
    