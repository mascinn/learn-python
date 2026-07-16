# if = Do some code only IF some condition is True
#      ELse do something

# Example 1
age = int(input("Enter your age: "))

if age >= 100:
    print("You are to old to signed up!")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You have'nt been born yet!")
else:
    print("You must be 18+ to sign up")


# Example 2
response = input("Would you like food? (Y/N: )")

if input == "Y":
    print("Have some food")
else:
    print("No food for you")

name = input("Whats your name: ")

if name == "":
    print("You did not type in your name")
else:
    print(f"Hello {name}")

# Example 3
isOnline = True

if isOnline:
    print("The user is online")
else:
    print("The user is offline")