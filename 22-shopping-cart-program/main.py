# Shopping cart program

foods = []
prices = []
items = 0
totalPrice = 0

while True:
    food = input("Enter the food to buy (Q/q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)
        totalPrice += price
    items +=1

print("--------Your Shopping Cart--------")
print("No.  Food            Price")

for item in range(items):
    print(f"{item + 1:<4} {foods[item]:<15} ${prices[item]:.2f}")

print(f"Total price is: ${totalPrice}")
    