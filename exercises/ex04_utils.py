"""Using 'list' Utility Functions."""

__author__ = "730569341"


def all(input: list[int], number: int) -> bool:
    """Given a list, whether or not all of the ints in the list are the same as the given int."""
    # start from first index
    i: int = 0
    # loop through each index of list
    if len(input) == 0:
        return False 
    while i < len(input): 
        if input[i] != number: 
            return False 
        i += 1 
    return True


def max(input: list[int]) -> int:
    """Given a list, return the largest number in the list."""  
    mymax = input[0]
    for number in input:
        if mymax is None or number > mymax:
            mymax = number
    return mymax
    # test if the list is empty
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    

def is_equal(list1: list[int], list2: list[int]) -> bool:
    """Given a two list, return if every element at every element is eqaul to both lists."""
    index_lists: int = 0 
    if len(list1) != len(list2):
        return False
    while index_lists < len(list1) and index_lists < len(list2): 
        if list1[index_lists] != list2[index_lists]: 
            return False
        index_lists += 1
    return True 
