"""Using 'list' Utility Functions."""

__author__ = "730569341"

#given a list, whether or not all of the ints in the list are the same as the given int
def all(input: int, number: int) -> bool: 
    # start from first index
    i: int = 0
    # loop through each index of list
    while i < len(input):
        #test if the item at this index is equal to number
        if input[i] == number: 
            return True 
        i+=1
    else: 
        return False 

#given a list, return the largest number in the list 
def max(input:list[int]) -> int:
    mymax = input[0]
    for number in input:
        if number > mymax:
            mymax  = number
        return mymax
    else: 
        #test if the list is empty
        if len(input) == 0:
            raise ValueError("max() arg is an empty List")
    
#given a two list, return if every element at every element is eqaul to both lists
def is_equal(list1:int, list2:int) -> bool: 
    if len(list1) != len(list2):
        return False
    if len(list1) == len(list2):
        return True 
