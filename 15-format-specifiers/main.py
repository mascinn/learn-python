# format specifiers = {value:flags} format a value based on what
#                     flags are inserted

price1 = 3121.2313
price2 = -822121.31

# .(number)f = round to that many decimal places (fixed point)
print("1. .(number)f = round to that many decimal places (fixed point)")
print(f"Price 1 is: ${price1:.3f}")
print(f"Price 2 is: ${price2:.3f}\n")

# :(number) = allocate that many spaces 
print("2. :(number) = allocate that many spaces")
print(f"Price 1 is: ${price1:10}")
print(f"Price 2 is: ${price2:10}\n")

# :03 = allocate and zero pad that many spaces
print("3. :03 = allocate and zero pad that many spaces")
print(f"Price 1 is: ${price1:010}")
print(f"Price 2 is: ${price2:010}\n")

# :< = left justify
print("4. :< = left justify")
print(f"Price 1 is: ${price1:<10}")
print(f"Price 2 is: ${price2:<10}\n")

# :> = right justify
print("5. :> = right justify")
print(f"Price 1 is: ${price1:>10}")
print(f"Price 2 is: ${price2:>10}\n")

# :^ = center align
print("6. :^ = center align")
print(f"Price 1 is: ${price1:^10}")
print(f"Price 2 is: ${price2:^10}\n")

# :+ = use a plus sign to indicate positive value
print("7. :+ = use a plus sign to indicate positive value")
print(f"Price 1 is: ${price1:+}")
print(f"Price 2 is: ${price2:+}\n")

# := = place sign to leftmost position
print("8. := = place sign to leftmost position")
print(f"Price 1 is: ${price1:=}")
print(f"Price 2 is: ${price2:=}\n")

# :  = insert a space before possitive numbers
print("9. :  = insert a space before possitive numbers")
print(f"Price 1 is: ${price1:=}")
print(f"Price 2 is: ${price2:=}\n")

# :, = comma separator
print("10. :, = comma separator")
print(f"Price 1 is: ${price1:,}")
print(f"Price 2 is: ${price2:,}\n")

# combination
print("11. combination")
print(f"Price 1 is: ${price1:+,.2f}")
print(f"Price 2 is: ${price2:+,.2f}\n")