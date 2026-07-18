# for loops = execute a block of code a fixed number of times.
#             you can't iterate over a range, string, sequence, etc.

# creditCards = "1234-5678-1011"

# for x in creditCards:
#     print(x)

for x in range(1, 11):
    if x == 4:
        continue
    elif x == 9:
        break
    else:
        print(x)