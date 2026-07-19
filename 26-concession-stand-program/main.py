# concession stand program

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn": 6.00,
        "fries": 2.50,
        "chips": 1.00,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25}

cart = {}
total = 0

print("--------------MENU--------------")
for key, value in menu.items():
    print(f"{key}: ${value}")
print("--------------------------------")

while True:
    food = input("Select an item (q to quit): ")
    if food.lower() == "q":
        break
    elif food in menu:
        cart[food] = menu[food]

print("---------Your Order---------")
for key, value in cart.items():
    print(f"{key:15}: ${value:.2f}")

for food in cart:
    total += cart[food]

print(f"Total is       : ${total:.2f}")