# The while loop

# The game rules
print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")

# Imports the random module.
import random

# Generates a random Integer between 1 and 10.
number = random.randint(1,10)

# Initializes the needed variables for the game.
isGuessRight = False

# Runs the guessing game.
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is right! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))

# The for loop
print("Let’s count to 10!")
for x in range (0, 11):
  print(x)