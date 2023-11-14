"""One Shot Wordle"""
__author__= "730671567"

White_box: str = "\U00002B1C"
Yellow_box: str = "\U0001F7E8"
Green_box: str = "\U0001F7E9"

secret_word = "python"
guess_word = len(secret_word)

guess = input('What is your 6-letter guess? ')
guess2 = len(guess)

while guess2 != guess_word: 
    
    print("That was not 6 letters! Try again: ")
    guess = input('What is your 6-letter guess? ')
    guess2 = len(guess)
    
if guess == secret_word:
    print("Woo! You got it! ")
else:
    print("Not Quite. Play again soon! ")

#index of each letter

letter_ind: int = 0

while letter_ind < len(guess):
    guess_let = guess[letter_ind]
    if (secret_word[letter_ind] == guess_let):
        print(Green_box, end="")
    else:
        contained: bool = False
        guessed = True
        index2: int = 0
        while index2 < 6:
            if (guess_let == secret_word[index2]):
                contained = True
            index2 = index2 + 1
        if contained:
            print(Yellow_box, end="")
        else:
            print(White_box, end="")
    letter_ind = letter_ind + 1
        
             