# List

# Tuple
print("----------Tuple----------")
# thistuple = ("apple", "banana", "orange", "orange", 123, True)
thistuple = tuple(("apple", "banana", "orange"))
print(thistuple)
print(len(thistuple))
onetuple = ("apple",)
print(type(onetuple))
nottuple = ("apple")
print(type(nottuple))

# Set
print("\n----------Set----------")
# thisset = {"banana", "apple", "orange", "apple", True, 123}
thisset = set(("banana", "apple", "berry"))
print(thisset)
print(len(thisset))
print(type(thisset))
trueset = {True, 1, 0, False}
print(trueset)

# Dictionary
print("\n----------Dictionary----------")
# thisdict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964,
#     "electric": False,
#     "colors": ["red","white","blue"]
#     # "year": 2020
# }
thisdict = dict(name = "John", age = 36, contry = "Norway")
print(thisdict)
print(thisdict["name"])
print(len(thisdict))
print(type(thisdict))