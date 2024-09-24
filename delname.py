# del keyword

# used to delete obj properties or obj itself

# del s1.name
# del s1


class Student:
    name = "Karan"
    age = 23

s1 = Student()
print(s1.name)


s2 = Student()
print(s2.age)

del s1
del s2
print(s2.age)
