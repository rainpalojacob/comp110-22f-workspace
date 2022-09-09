"""EXO1 - Chardle - A cute step toward Wordle."""

__author__ = "730569341"


first_word: str = input("Enter a 5-character word: ")
if len(first_word) < 5: 
    print("Error: Word must contain 5 characters ")
    exit
if len(first_word) > 5: 
    print("Error: Word must contain 5 characters ")
    exit  
if len(first_word) == 5: 
    first_char: str = input("Enter a single character: ")
if len(first_char) > 1:
    print("Error: Character must be a single character ")
    exit
print("Searching for " + first_char + " in " + first_word)


i: int = 0 

if first_char == first_word[0]: 
    print(first_char + " found at index 0 ")
    i = i + 1 
if first_char == first_word[1]:
    print(first_char + " found at index 1 ")
    i = i + 1 
if first_char == first_word[2]:
    print(first_char + " found at index 2 ")
    i = i + 1 
if first_char == first_word[3]:
    print(first_char + " found at index 3 ")
    i = i + 1 
if first_char == first_word[4]:
    print(first_char + " found at index 4 ")
    i = i + 1 

if i == 0:
    print("No instances of " + first_char + " found in " + first_word)
if i == 1:
    print("1 instance of " + first_char + " found in " + first_word)
if i == 2:
    print("2 instances of " + first_char + " found in " + first_word)
