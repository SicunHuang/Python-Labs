"""
CSCI 150 Lab 1

Name: Sicun Huang
Section (A or B): A

Creativity:
1. a dollars_to_euros function using euros_to_dollars function
2. the mpg_from_metric function utilizes functions already created
3. a pounds_to_dollars function 
"""

# ---------------------- 
# Section 1: Functions that return a value
# ----------------------


def euros_to_dollars(euros):
    """
    Convert a given amount of euro to dollars
    
    Args:
        euros: the amount in euros
    
    Returns:
        the equivalent amount in dollars
    """
    return euros * 1.21

def dollars_to_euros(dollars):
    """
    convert a given amount of dollars to euros
    
    Args:
        dollars: the amount in dollars
        
    Returns:
        the equivalent amount in euros
    """
    return dollars**2 / euros_to_dollars(dollars) 

def welcome():
    """
    Show a translation of “welcome” in welsh
    
    Args:
        none
    
    Returns:
        "welcome" in welsh
    """
    return ("croeso") 
        
def kilometers_to_miles(km):
    """
    Convert the distance kilometers into the equivalent distance in miles
    
    Args:
        km: the distance of kilometers
        
    Returns:
        The distance in of miles
    """
    miles_per_km = 0.621371
    return km * miles_per_km

def celsius_to_fahrenheit(C):
    """
    Convert the temperature in Celsius into Fahrenheit
    
    Args:
        C: the temperature in Celsius
        
    Returns:
        Temperature in Fahrenheit
    """
    return C * 1.8 + 32

def liters_to_gallons(L): 
    """
    Convert the number of liters into the equivalent amount in gallons
    
    Args:
        L: the number of liters
        
    Returns:
        The amount in gallons
    """
    gallons_per_liter = 0.264172
    return L * gallons_per_liter
        

def mpg_from_metric(km, L):
    """
    Show miles per gallon given the kilometers and liters
    
    Args:
        km: the distance in kilometers
        L: the number of liters
        
    Returns:
        Miles per gallon
    """
    return kilometers_to_miles(km) / liters_to_gallons(L)

def pounds_to_dollars(pounds):
    """
    Convert a given amount of pounds to dollars
    
    Args:
        pounds: the amount in pounds
    
    Returns:
        the equivalent amount in dollars
    """
    return pounds * 1.36 # 1 pounds = 1.36 dollars

# ---------------------- 
# Section 2: Functions that print
# ----------------------

def four_fours():
    """
    Express the values 0..9 using exactly four 4s.
    
    Allowed operators are +, -, *, //, %, **, and parentheses.
    
    Returns:
        None
    """
    print(4+4-4-4, "is 4+4-4-4")  # 0
    print(4//4-4+4, "is 4//4-4+4")  # 1
    print(4//4+4//4, "is 4//4+4//4")  #2
    print((4+4+4)//4, "is (4+4+4)//4")  #3
    print(4%(4+4+4), "is 4%(4+4+4)")  #4
    print(4**(4-4)+4, "is 4**(4-4)+4")  #5
    print((4+4)//4+4, "is (4+4)//4+4")  #6
    print(4+4-4//4, "is 4+4-4//4")  #7
    print(4+4-4+4, "is 4+4-4+4")  #8
    print(4+4+4//4, "is 4+4+4//4")  #9
    

def convert_from_seconds(seconds):     
    """
    Print number of days, hours, minutes, and seconds in a given number of seconds.
    
    Args:
        seconds: non-negative integer representing number of seconds
    
    Returns:
        None
    """
    days = seconds // (24 * 60 * 60) # Number of days
    leftover_seconds = seconds % (24 * 60 * 60) # The leftover seconds
    hours = leftover_seconds // (60 * 60) # Number of hours
    leftover_seconds2 = leftover_seconds % (60*60)
    minutes = leftover_seconds2 // 60 # Number of minutes
    leftover_seconds3 = leftover_seconds2 % 60 # Number of seconds 
    print(days, "days")
    print(hours, "hours")
    print(minutes, "minutes")
    print(leftover_seconds3, "seconds")
    
