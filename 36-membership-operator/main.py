# membership operator = used to test whether  a value or variable is found in a sequence
#                       (string, list, tuple, set, or dictionary)
#                       1. in
#                       2. not in

# word = "APPLE"

# letter = input("Guess a letter in the secret word: ")

# if letter not in word:
#     print(f"{letter} is not found")
# else:
#     print(f"There is a {letter}")

# students = {"Spongebob", "Pattrick", "Squidward"}

# student = input("Enter the name of a student: ")

# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# grades = {"Spongebob": "A", "Pattrick": "B", "Squidward":"C"}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

email = "makhasin@gmail.com"

if "@" and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")