"""EX07- Dictionary Functions."""

__author__ = "730569341"





def invert(given: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    # Given a dictionary a string, invert keys and values
    new_dictionary = dict[str, str] = dict()
    for key in given:
        if given[key] in new_dictionary:
            raise KeyError("Keys in dictionary must be unique.")
            new_dictionary[given[key]] = key 
    return new_dictionary


def favorite_color(given: dict[str, str]) -> str:
    """Find the most favored color."""
    # Given a dictionary of names and their favorite color, return which color appears the most
    favorite_color: str = ""
    new_dictionary: dict[str, int] = dict()
    max = 0

    for key in given:
        if given[key] in new_dictionary:
            new_dictionary[given[key]] += 1
        elif given[key] not in new_dictionary:
            new_dictionary[given[key]] = 1
        if new_dictionary[given[key]] > max:
            favorite_color = given[key]
            max = new_dictionary[given[key]]
    return favorite_color


def count(given: list[str]) -> dict[str, int]:
    """Count the number of times the key value appears in."""
    # Given a list of strings, return a dictionary where each key is a value in given list
    # Each value associated is the count/number of times that value appeared in given list
    new_dictionary: dict[str, int] = dict()
    # loop through each item in input list
    for key in range(len(given)):
        if given[key] in new_dictionary:
            new_dictionary[given[key]] += 1
        else:
            new_dictionary[given[key]] = 1
    return new_dictionary