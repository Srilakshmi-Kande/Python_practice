# dictionary
dictionary={
    "cat":"a small animal",
    "table":["a piece of furniture","list of facts & figures"]
}
print(dictionary)

# set
subjects={
    "pyhton","java","c++","python","javascript","java","python","java","c++","c"
}
print(subjects)

# dictionaries

marks={}
x=int(input("enter py : "))
marks.update({"phy":x})
x=int(input("enter chem : "))
marks.update({"chem":x})
x=int(input("enter math : "))
marks.update({"math":x})
print(marks)

values={9,9.0}
print(values)

values={9,"9.0"}
print(values)

values1={
    ("float",9.0),
    ("int",9)
}
print(values1)