# iterables =  an objects/collection that can return its elements one at a time,
#              allowing it to be iterated over in a loop

lists = [1,2,3,3,4,5]
for list in reversed(lists):
    print(list, end=" ")
print()

sets = (1,2,3,4,5)
for set in reversed(sets):
    print(set, end=" ")
print()

tuples = {1,2,3,3,4,5}
for tuple in tuples:
    print(tuple, end=" ")
print()

dictionary = {1:"satu", 2:"dua", 3:"tiga", 4:"empat", 5:"lima"}
for key in dictionary.values():
    print(key)