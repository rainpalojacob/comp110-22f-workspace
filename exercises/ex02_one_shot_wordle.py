"""Exercise 2 One shot wordle"""

__author__ = 730569341


secret: str = "python"
guess: str = input("What is your 6-letter guess? ")
# looping index
i: int = 0 
s: str = ""

# whether the guessed character exists 
exists: bool = False
# alternate indicies 
alt: int = 0

# checking indices for correct matches 
while i < len(secret): 
    if guess[i] == secret[i]:
        s+= "\U0001F7E9"
    else: 
        if alt == guess[i]: 
            exists = True 
            s+= "\U0001F7E8"
        else: 
            alt += 1 
        s+= "\U00002B1C"
    i+= 1 
print(s)

# prompting a guess
while len(guess) != len(secret): 
    guess: input("That was not 6 letters! Try again: ")  
else: 
    if guess != secret: 
        print("Not quite. Play again soon! ")
        exit
    if guess == secret:
        print("Woo! You got it! ")


        







   
   
  
  
  






