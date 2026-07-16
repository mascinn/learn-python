# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
age = int(input("Enter your age: "))

while name == "":
    print("You didn't enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

while age < 0:
    print("Age can't  be negative")
    age = int(input("Enter your age: "))
print(f"You are {age} years old")

food = input("Enter a food you like  (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter a food you like  (q to quit): ")
print("Bye")

num = int(input("Enter a number between 1 - 10: "))

while num < 1 or num > 10:
    print(f"number is not valid")
    num = int(input("Enter a number between 1 - 10: "))
print(f"your number is {num}")