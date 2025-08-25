"""
CSCI 150 Lab 6

Name: Sicun Huang 
Section: A

Creativity:

"""
from random import randint 

def read_words(filename):
    """
    Read file into a list of words
    
    Args:
        filename: path to file
    
    Return:
        List of words
    """
    with open(filename, "r") as file:
        wordlist = []
        for line in file:
            wordlist.append(line.strip())    
        return wordlist

def set_to_string(wordset):
    """
    Convert set into string, with each letter capitalized and separated by a space.
    
    Args:
        wordset: Set containing letters
    
    Return:
        String of letters
    """
    result = ""
    for element in wordset:
        result = result + element + " "
    return result.upper()
    
def insert_letter(letter,underscore,ans):
    """
    Fill in all occurence of letter in the underscored word by comparing underscore and ans
    
    Args:
        letter: Letter for guessing
        underscore: Current underscored word
        ans: Word to be guessed 
    
    Return:
        A new version of underscore with all occurences of the letter filled in (if the letter is in the word)
    """
    result = ""
    if letter in ans:
        for w in range(len(ans)):
            if letter != ans[w]:
                result += underscore[w]
            if letter == ans[w]:
                result += letter
    else:
        result = underscore 
         
    return result 
              
def play_wordgame(filename,guess):
    """
    Initiate the guessing game and continue until the game finishes
    
    Args:
        filename: Path to file containing the candidate letters
        guess: Number of incorrect guesses the player gets
    
    """
    wordlist = read_words(filename)
    index = randint(0, len(wordlist)-1)
    guess_word = wordlist[index]
    underscored_word = ""
    for i in range (len(guess_word)):
        underscored_word += "_" #find a word and transform it into underscores
    guessed_letters = set()
    count = 0
    while guess != 0 and underscored_word != guess_word:
        print("-----------------")
        print("Guessed letters: " + set_to_string(guessed_letters))
        print("Incorrect guesses left: " + "*" * guess)
        print("Word: " + underscored_word)
        print("")
        letter = input("Guess a letter: ")
        while letter in guessed_letters:
            print("Letter already guessed!")
            letter = input("Guess a letter: ")
        if letter in guess_word:
            underscored_word = insert_letter(letter,underscored_word,guess_word)
            guessed_letters.add(letter)
        else: 
            underscored_word = insert_letter(letter,underscored_word,guess_word)
            guessed_letters.add(letter)
            guess -= 1
            count += 1
    if guess == 0:
        print("The word was: " + guess_word)
        print("Better luck next time!")
    elif underscored_word == guess_word:
        print("You win!")
        print("The word was: " + guess_word)
        print("You guessed it with " + str(count) +" incorrect guesses")
        

if __name__ == '__main__':
    # When you are ready to start running your game when you click the green arrow,
    # delete the pass statement below and add a call to your play_wordgame() function
    play_wordgame("cs_words.txt", 7)
