# Typecasting = the procces of converting a variable from one data type to another
#                str(), int(), float(), bool()

name = "makhasin"
age = 21
gpa = 3.70
is_student = True

print(type(name))
print(type(age))
print(type(gpa))
print(type(is_student))

gpa = int(gpa)
print(gpa)

age = str(age)
age += "1"
print(age)

name = bool(name)
print(name)