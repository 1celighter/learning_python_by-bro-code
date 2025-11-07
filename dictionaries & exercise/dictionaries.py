# dictionary = a collection of {key:value} pairs
# ordered and changeable. No duplicates

capitals = {
    "USA": "Washington D.C",
    "India": "New Delhi",
    "China": "Beijing",
    "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals)) we can check if we need help 

# if we need gets up some value from dictioaniry we can use 

print(capitals.get("USA"))  

print(capitals.get("India"))

# if we dont have this value we will get none

print(capitals.get("Japan"))

# we also can use function with dictionaries

if capitals.get("Russia"):
    print("This county exist")
else:
    print("This capital doesnt exit")

# disctionaries update!

capitals.update({"Germany": "Berlin"})

print(capitals)

capitals.update({"USA": "Detroit"})

print(capitals)

# to remove key value pair we can use pop method 

capitals.pop("China")

print(capitals)

# we can remove latest key value pair with popitem method

capitals.popitem()

print(capitals)

# we can print only keys 

keys = capitals.keys()
print(keys) 

# and we will see only keys 

# and also we can iterate it with loop 

for key in capitals.keys():
    print(key)

# to get all our values in keys we can use it 

values = capitals.values()
print(values)

# or we can use iterate 

for value in capitals.values():
    print(value)

# dictionaries with 2d lists 

items = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")