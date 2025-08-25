"""
CS 150 function and docstring examples
"""

def interest_calculator(principal, rate_as_percent):
    """
    Compute interest earned
    
    Args:
        principal: Amount of initial money
        rate_as_percent: Interest rate as percentage, i.e. in range (0,100]
        
    Returns:
        Amount of interest earned
    """
    rate = rate_as_percent * 0.01
    return principal * rate

def dog_years(human_years):
    """
    Convert human years to dog years
    
    Args:
        human_years: Number of human years
        
    Returns:
        Number of dog years
    """
    return human_years * 7

def dog_stats(dog_name, years):
    """
    Print the name and age of a dog
    
    Args:
        dog_name: Name of dog
        years: Age of dog in years
    """
    print(dog_name, "is the name of the dog")
    print(dog_name, "is", years, "years old")

def advanced_dog_stats(dog_name, years):
    """
    Print basic dog information and then age in dog years
    
    Args:
        dog_name: Name of dog
        years: Age of dog in years
    """
    dog_stats(dog_name, years) #has print so don't need print command 
    print("In dog years that is " + str(dog_years(years)) + " years old")
    #callback to def dog_years(human_years) and def dog_stats(dog_name, years)
