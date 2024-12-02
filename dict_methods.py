mydict={
    "name" : "AparnaDevi",
    "subjects" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 95
    }
}

# mydict.keys()   # returns all key values
print(mydict.keys())

# mydict.values() # returns all values
print(mydict.values())

print(list(mydict.values()))

# mydict.items()  # returns all(key,val) pairs as tuples
print(mydict.items())

print(list(mydict.items()))

pairs=list(mydict.items())
print(pairs[0])

# mydict.get("key")  # returns the key according to value

print(mydict["name"])
print(mydict.get("name"))

# print(mydict["name2"])      # error
print(mydict.get("name2"))   # no error -> none

mydict.update({"city":"delhi"})
print(mydict)

# or

new_dict={"city":"delhi"}
mydict.update(new_dict)
print(mydict)