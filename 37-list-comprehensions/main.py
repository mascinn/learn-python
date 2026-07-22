#List comprehensions = A concise way to create lists in Python
#                      Compact and easier to read than traditional loops
#                      [expression for value in iterable if condition]

# traditional methode
doubles = []
for x in range(1,11):
    doubles.append(x * 2)
print(doubles)

# with list comprehensions
triples = [x * 3 for x in range(1,11)]
squares = [y * y for y in range(1,11)]

print(triples)
print(squares)

fruits = ["apple", "banana", "coconut", "orange"]
fruits = [fruit.capitalize() for fruit in fruits]
fruit_chars = [fruit[0] for fruit in fruits]

print(fruits)
print(fruit_chars)

numbers = [1, -2, 3, 0, -4, 5, -6]
possitive_nums = [num for num in numbers if num >= 0]
negative_nums = [num for num in numbers if num < 0]
even_nums = [num for num in numbers if num % 2 == 0]
odd_nums = [num for num in numbers if num % 2 == 1]

print(possitive_nums)
print(negative_nums)
print(even_nums)
print(odd_nums)

grades = [80, 22, 56, 77, 43, 14, 71]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)