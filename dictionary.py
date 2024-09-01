# Dictionary in python
# Dictionaries are used to store data value in key:value pairs
# they are unordered , mutable (changable) and don't allow duplicates key

# eg 
# dict = {
#     "name": "mg",
#     "cgpa": 9.8
#     "marks": [98,78,98],   
# }
# dict["name"]

# dict["key"] = "value" # to assign or add new

info = {
    "key": "value",
    "name": "MG",
    "sub": ['maths', 'science'],
    "topics": ("dict","set"),
    "Learn": "code",
    "age": 18,
    "is_adult": True,
    "marks": 99
}
null_dict = {}
print(info)
print(type(info))
info["age"] = 23
print(info)

# Nest dictionaries

student = {
    "name": "MG",
    "subjects": {
        "phy": 98,
        "chem": 98,
        "math": 98,    
    }
}
print(student)
print(student["subjects"]["chem"])
student["name"] = "ML"
print(student)

# dictionary methods 

# Return all keys 
# mydic.keys() 

# Return all values 
# mydic.values()

# return all (key,val) pairs as tuples 
# mydic.items()

# return the key according to value
# mydic.get("key")

# inserts  the specified items to the dictornary
# mydic.update(newDic)


# throws error in case of empty
print(student["name"])

# no error in case of empty , returns none
print(student.get("name"))

print(student.update({"city": "delhi"}))

print(student)
