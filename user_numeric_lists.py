"""
Purpose: To work with numeric lists in Python in realtion to basketball domain. 

Author: Alison Hatfield
Date 09-2023

"""

# import standard modules 
import statistics
import math


# TODO: import from local util_datafun_logger.py 
from util_datafun_logger import setup_logger

# TODO: Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)

# TODO: Create some shared data lists if you like - or just create them in your functions
average_points = [
    25,
    10,
    6,
    14,
    2,
    7,
    8,
    26,
    16,
    10,
    11,
    12,
    14,
    30,
    9,
    8,
    27,
    22,
    12,
    5,
]
# TODO: define some custom functions
minutes_played = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
points_scored = [2, 6, 9, 12, 16, 18, 20, 22, 26, 30]

#calcualte the mean, median, and mode
def illustrate_list_statistics():
    """This function illustrates descriptive statistics for a numric list."""

    logger.info(f"score_list: {average_points}")

    # Descriptive: Averages and measures of central tendency
    # Use statisttics module to get mean, median, mode
    # for a values list

    mean = statistics.mean(average_points)
    median = statistics.median(average_points)
    mode = statistics.mode(average_points)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

#calcualte the standard deviation and variance
    stdev = statistics.stdev(average_points)
    variance = statistics.variance(average_points)

    logger.info(f"stdev: {stdev}")
    logger.info(f"variance: {variance}")


def illustrate_list_correlation_and_prediction():
    """This function illustrates correlation and prediction for a numric list."""

    logger.info(f"minutes_played_list: {minutes_played}")
    logger.info(f"points_scored_list: {points_scored}")


    #claculate the correlation between minutes_played and points_scored
    correlation = statistics.correlation(minutes_played, points_scored)
    logger.info(f"correlation between minutes played and points scored: {correlation}")

    # Predictive: Machine Learning - Linear Regression
    # If the corrlation is close to 1.0, then the data is linearly related
    # If so, use statistics module to get linear regression for list1 and list2
    # This is a form of supervised machine learning - it uses all known data
    # Use the slope and intercept and an unknown (future) x to predict a y value
    # Python functions can return multiple values

    slope, intercept = statistics.linear_regression(minutes_played, points_scored)
    logger.info(f"The equation of the best fit line is: y = {slope}x + {intercept}")

    # Once we have learned the slope and intercept
    # of the best-fit straight line through the data,
    # we can use it to make predictions

    # Predict the y value for a given x value outside the range of the data

    x_max = max(minutes_played)
    future_time = 15
    newx = x_max * future_time  # predict for a future x value

    # Use the slope and intercept to predict a y value for the future x value
    # y = mx + b

    newy = slope * newx + intercept

    logger.info(f"We predict that when minutes played (x) = {newx}, points scored (y) will be about {newy}")

def illustrate_list_built_in_functions():
# Use Python built in funtions: min(), max(), len(), sum(), average, set(), sorted(), sorted() using reverse=Ture
    
    # min() and max() of average_points and return values
    max_average= max(average_points)
    min_average = min(average_points)

    logger.info(f"Given score list: {average_points}")
    logger.info(f"The max() is {max_average}")
    logger.info(f"The min() is {min_average}")

    # len() of average points and return the value
    len_list = len(average_points)
    logger.info(f"The len() is {len_list}")

    # sum() of average_points
    sum_list = sum(average_points)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the average_points
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {average_points}")
    # Return a new list soreted in ascending order
    asc_average_points = sorted(average_points)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_average_points}")

    # Return a new list soreted in descending order
    desc_average_points = sorted(average_points, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_average_points}")

def illustrate_list_methods():
    """This function illustrates methods that can be called on a list"""

    # append a single value to the list
    average_points.append(12)

    # extend the list with another list you pass in
    average_points.extend([4, 5, 6])

    # insert() at an index, insert a value
    i = 7
    newvalue = 16
    average_points.insert(i, newvalue)

    # rremove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    item_to_remove = 5
    average_points.remove(item_to_remove)

    # count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
    ct_of_2 = average_points.count(2)

    # Sort the list in ascending order using the sort() method
    asc_average_points2 = average_points.sort()

    # Sort the list in descending order using the sort() method
    desc_average_points2 = average_points.sort(reverse=True)

    # Copy()
    new_average_points = average_points.copy()
    logger.info(f"new_scores is: {new_average_points}")

    # pop() the first item off the top of the list/stack
    first = new_average_points.pop(0)
    logger.info(
        f"Popped the first (index=0): {first} and now, new_scores is: {new_average_points}")

    # pop() the last item off the bottom of the list/stack
    last = new_average_points.pop(-1)
    logger.info(
        f"Popped the last (index=-1): {last} and now, new_scores is: {new_average_points}")

 
def illustrate_list_transformations():
    """This function illustrates transformations that can be applied to a list"""

    logger.info(f"score_list: {average_points}")

    # Use the built in filter() function to keep x such that x is greater than 15 
    # (or some other cutoff), or keep the even ones, whatever.
    scores_over_15 = [filter(lambda x: x > 15, average_points)]
    logger.info(f"Scores over 15: {scores_over_15}")

    # Use the built-in function map() anywhere you need to transform a list

    # Use the built in map() function to map each x to cuberoot of x (hint: use math module)
    cbrt_scores = map(lambda x: math.cbrt(x), average_points)
    logger.info(f"Cube root of scores: {cbrt_scores}")

    # Use the built in map() function to calculate the volume of a cube with a 
    # side equal to the value in your list. Hint: Volume = side * side * side
    logger.info(f"Volume list: {average_points}")
    volume_list = [map(lambda x: x * x * x, average_points)]
    logger.info(f"Volume of Scores: {volume_list}")

def illustrate_list_comprehensions():
    """This function illustrates list comprehensions"""

    logger.info(f"score_list: {average_points}")

    # Use a list comprehension to filter (start within square brackets) to get x (for each x in list1) 
    # if x is less than 4 or some other cutoff
    scores_over_12 = [x for x in average_points if x > 12]
    logger.info(f"Scores over 12 (using list comprehensions!): {scores_over_12}")

    # Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1) 
    tripled_scores = [x * 3 for x in average_points]
    logger.info(f"Tripled scores (using list comprehensions!): {tripled_scores}")

    # Use a list comprehension to transform your numeric list into another numeric list using 
    # a transformation of your choice.
    sqrt_scores = [math.sqrt(x) for x in average_points]
    logger.info(f"The squareroot of the average points (using list comprehensions): {sqrt_scores}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    show_log()





