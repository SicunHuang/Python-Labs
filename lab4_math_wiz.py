"""
CSCI 150 Lab 4

Name: Sicun Huang 

Creativity:
1. add main_difficulty function that has three difficulty level (starting from line 91)

"""
from random import randint
import time

# Function definitions for math wiz

def random_equation(num):
    """
    generate a random math equations involving the numbers 1-10 and num number of operators +,-,*
    
    Args:
        num: the number of operators in the equation
    
    Returns:
        a string representing the random math equation 
    """
    operator = "+-*"
    equation = str(randint(1, 10))
    for i in range(num):
        equation += operator[randint(0,2)]+ str(randint(1, 10))
    return equation 

def query_equation(eq):
    """
    queries the user for the correct answer of the input equation until they get it right
    
    Args:
        eq: a string representing a mathematic equation
        
    Returns:
        print "Keep trying.", "Close. Try again.", and "Correct!" depending on user's answer
    """
    while True:
        answer = int(input(eq + "="))
        if answer == eval(eq):
            print ("Correct!")
            break
        elif (eval(eq) - 2) <= answer <= (eval(eq) + 2):
            print ("Close. Try again.")
        else: 
            print ("Keep trying.")

def play_game(sec, num):
    """
    presents the user new equations with num operator in a duration of sec seconds
    
    Args:
        sec: the game duration in seconds
        num: the number of operators
    
    Returns:
        print the number of correct answers and the actual time elapsed
    """
    t1 = time.time()
    x = 0
    while True:
        t2 = time.time()
        if (t2 - t1) < sec:
            query_equation(random_equation(num))   
            x = x + 1
        else: 
            print("You got " + str(x) + " correct in " + str(t2 - t1) + " seconds.")
            break
        
def main():
    """
    Launch the math wiz game by asking user if they want to play.
    If yes, ask for how long, and play until time is elapsed.
    If no, give a goodbye message.
    """
    reply = input("Do you want to play a game [yes/no]? ")
    if reply == "yes":
        s = int(input("How long do you want to play for [seconds]? "))
        n = int(input("How many operators do you want to have [1-10]? "))
        play_game(s, n) 
    else:
        print("Understandable. Have a great day!")
    
    
# Main program will be launched automatically when program is run
if __name__ == '__main__':
    main()
    
def main_with_difficulty():
    """
    Launch the math wiz game by asking user if they want to play.
    If yes, ask for how long and the difficulty of the game, and play until time is elapsed.
    If no, reply "Understandable. Have a great day!"
    """
    reply = input("Do you want to play a game [yes/no]? ")
    if reply == "yes":
        sec = int(input("How long do you want to play for [seconds]? "))
        difficulty = input("How difficult do want the game be [normal/difficult/hell]? ")
        if difficulty == "normal":
            play_game(sec, 2)
        elif difficulty == "difficult":
            play_game(sec, 5)
        elif difficulty == "hell":
            play_game(sec, 10)
    elif reply != "yes":
        print("Understandable. Have a great day!")
