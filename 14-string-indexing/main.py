# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start: end: step]

numberPhone = "1234-5678-9110"

print(numberPhone[0:4])
print(numberPhone[:4])
print(numberPhone[5:8])
print(numberPhone[5:])
print(numberPhone[-1])

print(numberPhone[::2])
print("\n\n")

# Example
creditNumbers = "2121-2121-2413-4124"
lastDigits = creditNumbers[-4:]
reverseNums = creditNumbers[::-1]

print(f"xxxx-xxxx-xxxx-{lastDigits}")
print(f"reverse digits: {reverseNums}")