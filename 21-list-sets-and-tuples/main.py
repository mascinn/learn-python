# collection = single "variable" used to store multiple values
# List = [] ordered and changeable, Duplicates OK
# Set = {} unordered and immutable, but Add/Remove OK, NO dulicates 
# TUple = () ordered and unchangeable Duplicates Ok, FASTER

# List
# fruits = ["apple", "orange", "banana", "coconut"]

# print(fruits[::-1])
# print(fruits[0:3])
# # print(fruits[4]) # index error
# print(len(fruits))
# print("apple" in fruits)
# print("pineaple" in fruits)

# fruits[0] = "pineaple"
# fruits.append("grape")
# fruits.remove("orange")
# fruits.insert(6, "avocado")
# fruits.sort()
# fruits.reverse()
# # fruits.clear()

# for fruit in fruits:
#     print(f"{fruits.index(fruit)}: {fruit}")

# print(fruits.count("grape"))
# # print(dir(fruits))

# Sets
# fruits = {"apple", "orange", "coconut", "banana", "banana"}

# print("apple" in fruits)

# fruits.add("pear")
# fruits.remove("apple")
# fruits.pop()
# # fruits.clear()

# # print(fruits[0]) # error because unordered
# print(fruits)

# Tuple
fruits = ("apple", "orange", "coconut", "banana", "banana")

print(fruits.index("orange"))
print(fruits.count("banana"))
print(fruits)

for fruit in fruits:
    print(f"{fruits.index(fruit)}: {fruit}")