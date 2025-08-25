"""
CSCI 150 Lab 5

Name: Sicun Huang  

Creativity: 

"""

"""
Enter file to analyze[().txt]: Toy_Story_Rating.txt
File contained 2077 entries
Max: 5
Min: 1
Average: 4.146846413095811
Median: 4
Std. dev: 0.8523490842765928

Analysis:
This data include 2077 viewer's ratings on the movie Toy Story
on a scale from 1 to 5. Ratings in this data set range from 5 to 1.
However, it has an approximate average of 4.14 and a median of 4, indicating
that this movie is overall well-received. Adding on to that, a standard
deviation of arond 0.85 shows viewers' attitudes are somewhat homogeneous 
"""

"""
Enter file to analyze[().txt]: 95kids.txt
File contained 35326 entries
Max: 9
Min: 0
Average: 0.43285398856366414
Median: 0.0
Std. dev: 0.8975902261262514

Analysis:
The data record the number of kids in each of 35326 households
in the Northeast region of the US in 1995. The largest number of kids
in one household amounts to 9, while some families have no kid.
The data also indicate an average of 0.432 kid per household in this region.
A standard deviation of 0.897 suggests households generally have 0-1 kid.
"""

import math 

def data_analysis():
    """Print out various various statistics about a data file contaning one number per line"""
    filename = input("Enter file to analyze[().txt]: ")
    data_stats(filename)

def data_stats(filename):
    """
    Print out various statistics about numbers in file.
    
    Assumes one number per line.
    
    Args:
        filename: Path to file
    """
    numlist = read_file(filename)
    print_stats(numlist)
    
def read_file(filename):
    """
    Read file into list of numbers assuming one number per line.

    Args:
        filename: Path to file
        
    Return:
        List of numbers
    """
    with open(filename, "r") as nums_file:
        numlist = []
        
        for line in nums_file:
            numlist.append(int(line.strip()))    
        
        return numlist

def largest_value(numlist):
    """
    Find the largest value in a list of numbers
    
    Args:
        numlist: List of numbers
    
    Return:
        Largest number in the list
    """
    return max(numlist)

def smallest_value(numlist):
    """
    Find the smallest value in a list of numbers
    
    Args:
        numlist: List of numbers
    
    Return:
        Smallest number in the list
    """
    return min(numlist)

def average_value(numlist):
    """
    Compute the average value of a list of numbers
    
    Args:
        numlist: List of numbers
        
    Return:
        Average value of the numbers as a float
    """
    return sum(numlist) / len(numlist)

def sta_dev(numlist):
    """
    Compute the standard deviation of a list of numbers
    
    Args:
        numlist: List of numbers
    
    Return:
        Standard deviation of the list as a float
    """
    sum_of_diff = 0
    for x in numlist:
        sum_of_diff = sum_of_diff + (x - average_value(numlist)) ** 2
    return math.sqrt(sum_of_diff / (len(numlist)-1))

def median(numlist):
    """
    Return middle value in non-empty sequence.
    
    Args:
        numlist: List of numbers
        
    Return:
        The middle element if sequence has odd length, or the average
        of the two middle elements if sequence has even length
    """
    numlist.sort()
    if len(numlist) % 2 == 1:
        return numlist[len(numlist) // 2]
    else:
        return (numlist[len(numlist) // 2] + numlist[len(numlist) // 2 - 1]) / 2
    
def print_stats(numlist):
    """
    Print out various statistics about the input list of numbers    
    Args:
        numlist: List of numbers
    """
    print("File contained " + str(len(numlist)) + " entries")
    if len(numlist) > 0:
        print("Max: " + str(largest_value(numlist)))
        print("Min: " + str(smallest_value(numlist)))
        print("Average: " + str(average_value(numlist)))
        print("Median: " + str(median(numlist)))
        print("Std. dev: " + str(sta_dev(numlist)))
        
def frequencies(data):
    """
    Attempts to print the frequency of each item in the list data
    
    Args:
        data: List of "sortable" data items
    """
    data.sort()
    
    count = 0
    previous = data[0]

    print("data\tfrequency") # '\t' is the TAB character

    for d in data:
        if d == previous:
            # Same as the previous, increment the count for the run
            count += 1
        else:
            # We've found a different item so print out the old and reset the count
            print(str(previous) + "\t" + str(count))
            count = 1
        
        previous = d
        
    print(str(previous) + "\t" + str(count))

        
# Main program that gets executed when program is run
# (Leave this as is, no changes to be made)
if __name__ == '__main__':
    # This invokes the data_analysis function when the program is run
    data_analysis()
