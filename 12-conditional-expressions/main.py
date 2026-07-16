# conditional expressions = A one-line shortcut for the if-else statement(ternary operator)
#                           Print or assign one of two values based on a condition 
#                           X if condition else Y

# Example 1
num = 9
print(f"Possitive" if num > 0 else "Negative")

result = "Even" if num % 2 == 0 else "Odd"
print(result)


# Example 2
a = 7
b = 10
maxNum = a if a > b else b
minNum = a if a < b else b

print(minNum)

# Example 3
age = 11
status = "Adult" if age >= 18 else "Child"
print(status)

# Example 4
temperature = 19
weather = "Hot" if temperature > 20 else "Cold"
print(weather)

# Example 5
userRole = "admin"
accesLevel = "Full Access" if userRole == "admin" else "Limited Access"
print(accesLevel)