"""Structured Woordle."""

__author__ = "730569341"


def contains_char(secret: str, char2: str) -> bool: 
    """Returning if a character is present within a given word.""" 
    assert len(char2) == 1
    i: int= 0
    for char in secret:
        if (char == char2):
            return True
        i+=1
    return False 


def emojified(guess: str, secret1: str) -> str:
    """Displaying the presence of character in guess with an emoji. """
    assert len(guess) == len(secret1)

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    s: str = ""
    i: int = 0 

    while i < len(secret1): 
        if contains_char(secret1, guess[i]) is False: 
            s+= WHITE_BOX
        elif secret1[i] != guess[i]:
                s+= YELLOW_BOX
        else:
            s+= GREEN_BOX
    return s


def input_guess(expected_length: int) -> int: 
    """Given an expected length, prompt user for guess."""
    user_guess: str = input(f"Enter a {expected_length} character word: ")
    while len(user_guess) != expected_length:
        user_guess: str = input(f"That wasn't {expected_length} chars! Try again! ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    #establihing what is the secret word
    secret: str = "codes"
    expected_length: int = len(secret)
    user_guess: str= ""
    turn_number: int = 1
    while turn_number < 7:
        print(f"=== Turn {turn_number}/6 ===")
        guess = input_guess(5)  
        print(emojified(guess, secret1))
        if guess == secret: 
            print(f"You won in {turn_number}/6 turns!")
            return
    print("X/6 - Sorry, try again tomorrow!")
    return

if __name__ == "__main__":
    main()