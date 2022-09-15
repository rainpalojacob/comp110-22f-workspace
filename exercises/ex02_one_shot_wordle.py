"""Exercise 2 One shot wordle."""

__author__ = "730569341"

secret: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

# looping index and boxes string
i: int = 0 
box: str = ""

# input from user
guess: str = input("What is your 6-letter guess? ")
while len(str(guess)) != 6:
    secret = input("That was not 6 letters! Try again: ")
while len(str(guess)) == 6:
    print("Not quite. Play again soon! ")

# checking for incorrect matches
while i < len(secret):
   # whether the guessed character exists 
    exists: bool = False 
    # alternate indicies 
    s: int = 0 
    while s < len(secret):
        if guess[i] == secret[s]:
            exists = True
        s += 1    
            
    # checking indices for correct matches
    if guess[i] == secret[i]:
        box += GREEN_BOX
    elif exists:
        box += YELLOW_BOX
    else:
        box += WHITE_BOX
    i += 1 
print(box)
if box == GREEN_BOX * len(secret):
    print("Woo! You got it! ")