# in dictionary type all data types are allowed
info={              
    "key":"value",
    "name":"apnacollege",
    "learning":"coding",
    "age":35,
    "is_adult":True,
    "marks":94.4
}
print(info)

info2={
    "name":"apnacollege",
    "subjects":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True,        # all are acceptable
    12:94.4
}
print(info2)
print(type(info))
print(type(info2))

print(info2["name"])
print(info2["topics"])
print(info2["subjects"])
print(info2["age"])

# print(info["surname"])

info["name"]="Shradhakapra"
print(info)