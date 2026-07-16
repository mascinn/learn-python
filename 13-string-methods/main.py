# name = input("Your name: ")

# lenghtName = len(name)
# print(lenghtName)

# findAbjad = name.find("a")
# print(findAbjad)

# rFindAbjad = name.rfind("a")
# print(rFindAbjad)

# capitalize = name.capitalize()
# print(capitalize)

# upper = name.upper()
# print(upper)

# lower = name.lower()
# print(lower)

# isAplha = name.isalpha()
# print(isAplha)

# isNum = name.isdigit()
# print(isNum)
# print("\n\n")

# # Example 1
# phoneNumber = input("Enter your phone number ex.0812-3456-7891: ")

# stripCount = phoneNumber.count("-")
# replaceStrip = phoneNumber.replace("-", " ")
# print(phoneNumber)
# print(stripCount)
# print(replaceStrip)

# Example 2
# Validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

userName = input("Enter your username: ")

if len(userName) > 12:
    print("Your username can't be more than 12 characters")
elif not userName.find(" ") == -1:
    print("Your username can't contain spaces")
elif not userName.isalpha():
    print("Your username can't contain number")
else:
    print(f"Welcome {userName}")