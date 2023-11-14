"""EX01 - Finding a Letter in a 5 Letter Word"""
__author__ = "730671567"
x: int = 5
word = input("Enter a 5-character word: ")
word2 = len(word)
if word2 != x:
    print("Error: Word must contain 5 characters")
    exit()
else:
    letter = input("Enter a single letter: ")
    if len(letter) != 1:
        print("Error: Character must be a single character")
        exit()
print("Searching for " + letter + " in " + word)
index = 0
count = 0
while index < len(word):
    if (word[index]) == letter:
        count = count + 1
        print("" + letter + " found at index " + str(index))
        index = index + 1
    else:
        index = index + 1

if count == 1:
    print("" + str(count) + " instance of " + letter + " found in " + word)
else:
    if count > 1:
        print("" + str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


    