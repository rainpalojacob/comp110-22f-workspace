"""EX07- Dictionary Functions."""

__author__ = "730569341"


def invert(given: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    # Given a dictionary a string, invert keys and values
    new_dictionary = []
    for i in reversed(given): 
        given[i] = new_dictionary[i]
    return new_dictionary 


def favorite_color(given: dict[str, str]) -> str:
    """Find the most favored color."""
    # Given a dictionary of names and their favorite color, return which color appears the most
    for item in given:
        if item in given:
            given[item] += 1
        else:
            given[item] = 1 
    return max(given, key=given.get)


def count(given: list[str]) -> dict[str, int]:
    """Count the number of times the key value appears in."""
    # Given a list of strings, return a dictionary where each key is a value in given list
    # Each value associated is the count/number of times that value appeared in given list
    new_dictionary = []

    # loop through each item in input list
    for item in given:
        # if found in dict, increase value association with key by 1
        if item in given.keys():
            new_dictionary[item] += 1 
        # if not found in dict, then first time and assign count of 1
        else: 
            new_dictionary[item] = 1
    return new_dictionary 
