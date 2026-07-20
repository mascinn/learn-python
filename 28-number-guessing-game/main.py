# Python number guessing game
import random

lowestNum = 1
highestNum = 100
answer = random.randint(lowestNum, highestNum)
guesses = 0
isRunning = True

print("Python Number Guessing Game")
print(f"Select a number between {lowestNum} and {highestNum}")

while isRunning:

    guess = input("Enter your guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowestNum or guess > highestNum:
            print("That number is out of range")
            print(f"Select a number between {lowestNum} and {highestNum}")
        elif guess < answer:
            print("To low! try again")
        elif guess > answer:
            print("To high! try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            isRunning = False

    else:
        print("Invalud guess")
        print(f"Please select a number between {lowestNum} and {highestNum}")