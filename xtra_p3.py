"""
In this code we will compare two plays by analyzing the number of common words with a length greater than 10

Author: Alison Hatfield
Date 09-2023

>>> len(longwordset1)
415

>>> len(longwordset2)
197

>>> len(longwords)
13
"""

import doctest

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


def compare_two_plays():
    ''' This function compares two plays by Shakespeare.'''
    logger.info("Calling compare_two_plays()")
        
    # read from file and get a list of words

    with open("text_hamlet.txt", "r") as f1:
        text = f1.read()
        wordlist1 = text.split()  # split on whitespace

    logger.info(f"List of words from play 1: {wordlist1}")


    # read from file and get a list of words

    with open("text_juliuscaesar.txt", "r") as f2:
        text = f2.read()
        wordlist2 = text.split()  # split on whitespace

    logger.info(f"List of words from play 2: {wordlist2}")

    # Remove duplicates by creating two sorted sets
    wordset1 = sorted(set(wordlist1)) #removed duplictes by creating a sorted set of wordlist1
    wordset2 = sorted(set(wordlist2)) #removed duplictes by creating a sorted set of wordlist2


    # initialize a variable maxlen = 10
    maxlen = 10  

    # use a list comprension to get a list of words longer than 10
    longwordset1 = [word for word in wordset1 if len(word) > maxlen]
    longwordset2 = [word for word in wordlist2 if len(word) > maxlen]


    longwordset1 = set(longwordset1)
    longwordset2 = set(longwordset2)

    # find the intersection of the two sets
    longwords = longwordset1 & longwordset2

    # print the length of the sets and the list
    print(len(longwordset1))
    print(len(longwordset2))
    print(len(longwords))
    print()
    print(sorted(longwords))
    print()

    logger.info(f"{len(longwordset1) = }")
    logger.info(f"{len(longwordset2) = }")
    logger.info(f"{len(longwords) = }")


    # check your work
    print("TESTING...if nothing prints before the testing is done, you passed!")
    doctest.testmod()
    print("TESTING DONE")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    compare_two_plays()

    logger.info("Complete the code to compare two plays.")
    show_log()

