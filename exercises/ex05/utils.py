
"""EX05 'List' Utility Functions."""

__author__ = "730569341"


def only_evens(list: list[int]) -> list[int]:
    """Given a list of integers, display only even integers."""
    even_numbers = []
    # loop through each index of list 
    for number in list: 
        # check if the number is divisble by 2
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers 
  

def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Given two lists of integers, display list with all elements."""
    # empty list to store the elements from both lists
    result = []
    # appending elements of list_two at the end of list_one
    for element in list_one: 
        result.append(element)

    for element in list_two:
        result.apend(element)
     # concatenating based on list comprehension
    result = list_one + list_two
    return result
   
   
def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """Given a list of integers, display the subset of the given list."""
    subset: list[int] = []

    if start < 0:
        start = 0 
    
    if end > len(a_list): 
        end = len(a_list)

    i: int = 0
    while start < end:
        if len(a_list) == 0:
            return subset
        if start > len(a_list):
            return subset
        if end <= 0 :
            return subset 
    else: 
        return subset 
     