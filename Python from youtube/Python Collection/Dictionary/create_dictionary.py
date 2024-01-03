phones = {
    "tahsin" : 1068,
    "ridu" : 1100,
    "niloy" : 1065,
    "rizu" : 1014
}
print(phones)
# checking type of dictionary
print(type(phones))
# length of dictionary
print(len(phones))

# access items
print(phones["tahsin"])
print(phones.get("rizu"))

# print just keys / values
print(phones.keys())
print(phones.values())

# update value in dict
phones["tahsin"] = 5000
print(phones.keys())
print(phones.values())


# add elements in dict
phones["abrar"] = 1234
print(phones)


more_phones = {
    "tawsif" : 9655,
    "lilin" : 4321,
    "sharar" : 6645
}

phones.update(more_phones)
print(phones)


# remove elements in dict
phones.pop("ridu")
phones.pop("rizu")
phones.pop("niloy")
print(phones)

phones.popitem()
# this will remove the last item on the dict
print(phones)

# phones.clear() # this will empty the dictionary
# print(phones)

# looping through dictionary
for x,y in phones.items():
    print(x, y)

# nested dict

phones = {
    "Area1" : {
        "x" : 0,
        "y" : 1,
        "z" : 2
    },
    "Area2" : {
        "a" : 8,
        "b" : 7,
        "c" : 6
    }
}


print(phones["Area1"]["y"])
print(phones["Area2"]["c"])