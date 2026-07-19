# dictionary = a collection of {key:value} pairs
#              ordered and changeable. NO duplicates

capitals = {"USA": "Washington DC",
            "India": "New Delhi",
            "Indonesia": "Jakarta",
            "Australia": "Sydney",
            "Japan": "Tokyo"}

# print(dir(capitals))
# print(help(capitals))
print(capitals.get("USA"))

if capitals.get("USA"):
    print("That capital is exists")
else:
    print("That capital doesn't exists")

capitals.update({"Germany": "Berlin"})
capitals.update({"Germany": "Shanghai"})
# capitals.pop("USA")
# capitals.popitem()
# capitals.clear()
print(capitals)

keys = capitals.keys()
print(keys)
for key in capitals.keys():
    print(key)

values = capitals.values()
print(values)
for value in capitals.values():
    print(value)

items = capitals.items()
print(items)
for key, value in capitals.items():
    print(f"{key}: {value}")