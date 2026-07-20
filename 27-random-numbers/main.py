import random

low = 1
high = 100
option = ("rock", "paper", "scissors")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

randomNum = random.randint(low, high)
randomFloatNum = random.random() # random number between 0 - 1
choice = random.choice(option)
random.shuffle(cards)

print(randomNum)
print(randomFloatNum)
print(choice)
print(cards)