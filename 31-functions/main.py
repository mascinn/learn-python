# functions = A block of reusable code
#             place () after the function name to invoke it

def happy_birthday(name, age):
    print(f"Happy birthday to {name}!")
    print(f"You are {age} old!")
    print("Happy birthday to you!")
    print()

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount:.2f} is due: {due_date}")

happy_birthday("bro", 22)
display_invoice("coy", 100, "02/21")

# return = statement used to end a function
#          and send a result back to the caller

def add(x, y):
    z = x + y
    return z

def substract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(8, 4))
print(substract(8, 4))
print(multiply(8, 4))
print(divide(8, 4))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Makhasin", "Muhammad")
print(full_name)