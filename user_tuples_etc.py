"""
Purpose: Illustrate tuples, sets, and dictionaries in Python and relate it to the basketball domain. 

Author: Alison Hatfield
Date: 09-2023

"""
# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

def illustrate_tuples():
    """This function illustrates tuples in Python."""

    # Create some tuples (think database records, or Excel rows). Use the examples to practice with tuples.
    assists = (3, 3, 6, 8, 12)
    rebounds = (4, 4, 7, 9, 11)
    points = (5, 12, 12, 14, 16)

    logger.info(f"{assists = }")
    logger.info(f"{rebounds = }")
    logger.info(f"{points = }")

    # tuple concatenation
    assists_rebounds = assists +rebounds
    game_stats = assists + rebounds + points

    # tuple repetition
    points_3 = points * 3

    logger.info(f"{assists_rebounds = }")
    logger.info(f"{game_stats = }")
    logger.info(f"{points_3 = }")
    
    # tuple membership testing
    hasOne_assists = 1 in assists  # False
    has12_points = 4 in points  # True

    logger.info(f"Did a player have 1 assist? {hasOne_assists}")
    logger.info(f"Did a player score 12 points? {has12_points}")

#Sets: create two sets. Get the intersection and the union.
def illustrate_sets():

    assists2 = {2, 5, 7, 8, 10}
    rebounds2 = {3, 7, 9, 11, 12}

    logger.info(f"{assists2 = }")
    logger.info(f"{rebounds2 = }")

    # set union
    union_stats = assists2 | rebounds2

    # set intersection
    intersection_stats = assists2 & rebounds2

    # set difference
    dif_stats = assists2 - rebounds2

def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""

    Lebron_dict = {"name": "Lebron", "age": 38, "weight_lbs": 250, "height": "6'9"}
    Michael_dict = {"name": "Michael", "age": 60, "weight_kg": 216, "height": "6'6"}

    logger.info(f"{Lebron_dict = }")
    logger.info(f"{Michael_dict = }")

    player_dict = {
        "name": ["Lebron", "Michale", "Steph", "Scotty"],
        "age": [38, 60, 35, 62],
        "height": ["6'9", "6'6", "6'2", "6'3"],
    }
    logger.info(f"{player_dict = }")


    #Use a dictionary to create key-value pairs of each word and its count from a file.
    with open("text_dict_words.txt") as file_object:
        word_list = file_object.read().split()

    word_counts_dict = {word: word_list.count(word) for word in word_list}


    logger.info("Given text_dict_words.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict}")


def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

  
    show_log()