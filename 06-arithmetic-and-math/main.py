import math

# circumference of circle
radius = float(input("Enter the radius of a circle: "))

circumference = 2 * math.pi * radius
print(f"The circumference is: {round(circumference, 2)}cm")


# area of a circle
area = math.pi * pow(radius, 2)
print(f"The area is: {round(area, 2)}cm^2")


# phytagoras
a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))
print(f"Side C is: {c}")

# x = 3.14
# y = 7
# z = 9

# # result = round(x)
# # result = abs(y)
# # result = pow(4, 3)
# result = max(x, y, z)

# print(result)

# import math

# print(math.pi)
# print(math.e)

# x = 64.4

# srqt = math.sqrt(x)
# ceil = math.ceil(x)
# floor = math.floor(x)
# print(floor)