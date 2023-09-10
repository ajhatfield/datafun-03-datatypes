"""
Modify this docstring.

"""

# imports first

import random

from util_datafun_logger import setup_logger

# Set up logging 
logger, logname = setup_logger(__file__)

#Create about 5 lists 

# Define a list of players
list_players = ["Steph", "Michael", "Kobe", "Lebron", "Giannis", "Scotty", "Michael"]

# Define a list of outcomes
list_outcomes = ["win", "lose", "tie"]

# Define a list of teams
list_teams = ["team1", "team2"]

# Define a list for stats
list_stats = ["points", "assists", "rebounds"]

# Define a list of jersey colors
list_jersey_colors = ["black", "white", "red", "blue", "pink", "yellow"]

#Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.
def process_lists_sets_zips():

    unique_players = set(list_players)  # remove duplicate players names by making a set
    combo_lists = zip(list_teams, list_players)  #Cobined 2 list to make a tuple

    # Get the count and list of players
    player_ct = len(list_players)

    logger.info(f"The list of words is: {list_players}")
    logger.info(f"There are {player_ct} players listed.")

    logger.info(f"The combined list of players and teams is: {combo_lists}")
   

    # Print the count and list of unique players
    unique_player_ct = len(unique_players)

    logger.info(f"The set of unique words is: {unique_players}")
    logger.info(f"There are {unique_player_ct} unique words in the file.")

def create_random_sentence_and_value():
    #Use random.choice() to pick a random value from one of your lists.
    random_player = random.choice(list_players)

    logger.info(f"The best player listed is: {random_player}")

    #Customize the sentence generator to create random sentences about your domain.
    logger.info("Calling create_random_sentence()")

    # Create a random sentence
    game_details = (
        f"{random.choice(list_players)} plays for {random.choice(list_teams)} who wore " 
        f"{random.choice(list_jersey_colors)} jerserys and {random.choice(list_outcomes)}.")

    logger.info(f"Random sentence: {game_details}")


#Choose one of the text data files in the repo - or add another related your your domain.
def process_text_teams():
    """Read in text_teams_NBA.txt and process it"""
    logger.info("Calling process_teams_NBA.txt()")

    # read in teams to get a list of words
    #Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
    with open("teams_NBA.txt", "r") as fileObject:
        NBA_teams = fileObject.read()
        list_NBA = NBA_teams.split()  # split on whitespace
        unique_NBA_teams = set(list_NBA)  # remove duplicates by making a set

        #Sort the list. 
        sorted_NBA = list_NBA.sort
        logger.info(f"The sorted list of NBA teams is: {sorted_NBA}")

        #Use len() to get the length display it to the console.
        NBA_ct = len(list_NBA)

        logger.info(f"The list of words is: {list_NBA}")
        logger.info(f"There are {NBA_ct} words in the file.")

        # Print the count and list of unique words
        unique_NBA_ct = len(unique_NBA_teams)

        logger.info(f"The set of unique words is: {unique_NBA_teams}")
        logger.info(f"There are {unique_NBA_ct} unique words in the file.")


# reusable functions next
def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# -------------------------------------------------------------
# call functions and execute code
# use if __name__ == "__main__":
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    process_lists_sets_zips()
    create_random_sentence_and_value()
    process_text_teams()

    show_log()
  
