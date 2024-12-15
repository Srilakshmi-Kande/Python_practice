# empty dictionary
null_dict={}
print(null_dict)

null_dict["name"]="apnacollege"
print(null_dict)

# nested dictionaries

student={
    "name" : "Shradha",
    "subjects" : {
        "chem" : 98,
        "phy" : 97,
        "math" : 95
    }
}

m_marks=student["subjects"]["math"]
print(m_marks)

print(student)

print(student["subjects"])

print(student["subjects"]["chem"])