# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

name = input("Whats your name: ")
age = int(input("How old are you: "))

age += 1

print(f"Hello {name}")
print(f"Your Old is {age}\n\n")

# Exercise 1 Rectangle Area Calc
print("Rectangle area calc")
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area is {area}cm^2\n\n")

# Exercise 2 Shopping Cart Program
item = input("What item would you like to buy: ")
price = float(input("What is the price: "))
quantity = int(input("How many would you like: "))
total = price * quantity

print(f"You have bought {quantity} x {item}")
print(f"Your total is: ${total}")