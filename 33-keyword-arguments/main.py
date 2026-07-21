# keywords arguments = an argument preceded by an identifier
#                      help with readability
#                      order of arguments doesn't matter
#                      1. positional 2. DEFAULT 3. KEYWORD 4. arbitrary

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

hello("Hello", "Mr.", last="Squarepants", first="Spongebob")

for x in range(0, 10):
    print(x, end=" ") # end is built in keyword function in print function
print()

print("1", "2", "3", "4", "5", sep="-")

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country="+62", area=857, last=1652, first=5896)
print(phone_num)