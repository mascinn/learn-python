# nested loops = A loop within another loop (outer, inner)
#                outer loop:
#                   inner loop:

rows = int(input("Enter the # rows: "))
column = int(input("Enter the # column: "))
symbol = input("Enter a symbol to use: ")

for row in range(rows):
    for col in range(column):
        print(symbol, end="")
    print()