"""
CS 150 Lab 3

Name: Sicun Huang

Creativity: 
1. write the function named shift
2. write functions my_encrypt and my_decrypt 
"""

from random import randint, seed

ALPHABET = "abcdefghijklmnopqrstuvwxyz "

#---------------------------------------------------------
# Fools functions

def fools_encrypt(s):
    """
    Return string s with each character repeating 3 times
    
    Args:
        s: String message that needs to be encrypted     
    
    Returns:
        Encrypted message string
    """
    r =""
    for i in s:
        r = r + i * 3
    return r

# def fools_decrypt(s):
#     return s[::3]
    
#---------------------------------------------------------
# Caesar's method

def shift_letter(letter, num):
    """
    Shift a letter by num places in ALPHABET with wraparound
    
    Args:
        letter: Character to shift
        num: Integer amount to shift character in ALPHABET

    Returns:
        Letter shifted by num characters in ALPHABET
    """ 
    # Get the index of the current letter
    index = ALPHABET.find(letter)
    # We use the mod operator (%) for wraparound
    return ALPHABET[(index + num) % len(ALPHABET)]


def caesar_encrypt(message, num):
    """
    Shift all characters in string message by num places
    
    Args:
        message: String message to shift
        num: Interger amount to shift characters in message
        
    Returns:
        Encrypted message string
    """
    result = ""
    for i in message:
        replace = shift_letter(i, num)
        result = result + replace
    return result 
    
#---------------------------------------------------------
# Substitution cipher

def splice(message, letter):
    """
    Splice out letter from message and return remaining message

    For example:
    >>> splice("abcdefg", "f")
    'abcdeg'

    Args:
        message: String to remove letter from
        letter: Character that occurs exactly once in message
        
    Returns:
        message with letter removed

    """ 
    return message.replace(letter,'')


def keygen(password):
    """
    Generate a new random key using string password
    
    Args:
        password: String password used to generate key
    
    Returns:
        A key consisting of a random ordering of the letters in ALPHABET
    """
    remaining = ALPHABET
    key = ""
    
    seed(password)
    
    for _ in range(len(ALPHABET)):
        index = randint(0, len(remaining)-1)
        next_letter = remaining[index]
        key = key + next_letter
        remaining = splice(remaining, next_letter)
    
    return key
    
def subst_encrypt(message, key):
    """
    Encrypt the string message using the string key
    
    Args:
        message: String message that needs to be encrypted
        key: String consisting of a random ordering of the letters in ALPHABET
        
    Returns:
        the string message encrypted using the string key
    """
    result = "" 
    for i in message:
        replace = key[ALPHABET.find(i)]
        result = result + replace
    return result

def subst_decrypt(message, key):
    """
    Decrypt the string message using the string key
    
    Args:
        message: Encrypted string message 
        key: String consisting of a random ordering of the letters in ALPHABET
        
    Returns:
        the string message decrypted using the string key
    """
    result = "" 
    for i in message:
        replace = ALPHABET[key.find(i)]
        result = result + replace
    return result

def shift(num):
    """
    Return a key that is the in-order alphabet shifted up by num places
    
    Args:
        num: Interger amount to shift characters
    
    Returns:
        the in-order alphabet shifted up by num places
    """
    result = ""
    for i in ALPHABET:
        replace = shift_letter(i, num)
        result = result + replace
    return result

def my_encrypt(message):
    """
    Encrypt string message with each character turning into charcters with opposite index number
    
    Args:
        message: String message that needs to be encrypted
    
    Returns:
        encrypted message with each character turning into charcters with opposite index number
    """
    result = ""
    for i in message:
        index = ALPHABET.find(i)
        result = result + ALPHABET[-index]
    return result    #character "a" doesn't change; character "b" corresponds to space

def my_decrypt(message):
    """
    Decrypt string message with each character turning into charcters with opposite index number
    
    Args:
        message: String message that needs to be decrypted
    
    Returns:
        decrypted message with each character turning into charcters with opposite index number
    """
    return my_encrypt(message)
     