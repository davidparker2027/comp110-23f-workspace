"""Real Wordle."""
__author__ = "730671567"


def contains_char(guess: str, character: str) -> bool:  # Does guess contain a character of secret
    """Find out if a character is in the word."""
    assert len(character) == 1
    letter_idx: int = 0
    while letter_idx < len(guess):
        if guess[letter_idx] == character:
            return True
        letter_idx = letter_idx + 1
    return False


def emojified(guess: str, secret: str) -> str:  # Placing coloured boxes depending on guess
    """Testing to see if length of Guess = Secret as well as accuracy."""
    assert len(guess) == len(secret)
    letter_idx: int = 0
    White_box: str = "\U00002B1C"
    Yellow_box: str = "\U0001F7E8"
    Green_box: str = "\U0001F7E9"
    emojis: str = ""

    while letter_idx < len(guess):  # Defining if letters are the same or not
        guess_let: str = guess[letter_idx]
        if secret[letter_idx] == guess_let:
            emojis += Green_box
        else:
            if contains_char(secret, guess_let):  # Fixing the contains_char function call
                emojis += Yellow_box
            else:
                emojis += White_box
        letter_idx = letter_idx + 1
    return emojis
    

def input_guess(expected_length: int) -> str:  # Input guess + ensure same length as secret.
    """Get the guess from the user."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while True:
        if len(guess) == expected_length:
            return guess
        else:
            guess = input(f"That wasn't {expected_length} characters! Try again: ")


def main() -> None:
    """The entrypoint of the program and the main game loop."""
    # Run the program using defined functions
    secret: str = "codes"
    playing: bool = True
    turns: int = 0
    outcome: bool = False  # Move outcome variable outside the loop
    while playing and turns < 6:  # if playing = True and turns remaining stay in while loop
        if turns < 6:
            print(f" === Turn {turns + 1}/6 === ")
            guess_word: str = input_guess(len(secret))
            print(emojified(guess_word, secret))
            if guess_word == secret:
                outcome = True
                playing = False  # leave out of the loop if the correct guess is made
            else:
                turns = turns + 1
    if outcome:  # Solved correctly or not
        print(f"You won in {turns + 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
