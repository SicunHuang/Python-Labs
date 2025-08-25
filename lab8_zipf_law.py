"""
Takes a file name as command line argument to print up to the 10 most frequent words with their frequncies and a log-log plot of word count versus word rank. 

CSCI 150 Lab 8

Name: Sicun Huang 
Section: A

Creativity:

"""
import string 
import matplotlib.pyplot as plt
import sys

def read_corpus(filename):
    """
    read a file and return a list of words in this file 
    
    Args:
        filename: Name of file
        
    Return:
        List of words in a file without punctuation
    """
    wordlist1 = []
    with open(filename,"r", errors='ignore') as file:
        for line in file:
            wordlist1 += line.split()
        wordlist2 = []
        for word in wordlist1:
            wordlist2.append(word.lower().strip(string.punctuation))
    return wordlist2

def second_element(iterable):
    """
    return the second element of a iterable object
    
    Args:
        iterable: Iterable object
        
    Return:
        Element at the second index
    """
    return iterable[1]

def count_and_rank(wordlist):
    """
    returns a tuple containing a list of words and a list of counts for those words
    
    Args:
        wordlist: List of words
    
    Return:
        Tuple containing a list of words and a list of counts for those words in decreasing order
    """
    counts = {}
    for word in wordlist:
        counts[word] = counts.get(word,0) + 1
    list1 = []    
    for item in counts.items():
        list1.append(item)
    list2 = sorted(list1,key=second_element,reverse=True)
    wordlist = []
    countlist = []
    for element in list2:
        wordlist.append(element[0])
        countlist.append(element[1])
    return wordlist,countlist
    
def print_top_10(atuple):
    """
    print out the 10 most frequent words and their frequencies from a file
    
    Args:
        atuple: Tuple contaning two lists generated in function count_and_rank(wordlist)
    
    Print:
        First 10 elements in both lists seperated by a tab
    """
    print("Word","Count",sep="\t")
    for i in range(10):
        print(atuple[0][i],atuple[1][i],sep="\t")

def generate_plot(atuple):
    """
    generate a log-log plot of word count versus word rank
    
    Args:
        atuple: Tuple contaning two lists generated in function count_and_rank(wordlist)
    
    Print:
        Plot of count vs. rank of words
    """
    x = []
    y = []
    for i in range(1,len(atuple[0])+1):
        x.append(i)
    for count in atuple[1]:
        y.append(count)
    plt.plot(x,y,"bo")
    plt.yscale("log")
    plt.xscale("log")
    plt.xlabel("Rank")
    plt.ylabel("Count")
    plt.title("Log-log plot of count vs. rank of words in text corpus")
    plt.show()
    
def print_usage():
    """Print usage message for program"""
    print("usage: python3 zipf_law.py <filename>")
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print_usage()          
    else:
        filename = sys.argv[1]
        atuple = count_and_rank(read_corpus(filename))
        print_top_10(atuple)
        generate_plot(atuple)
        