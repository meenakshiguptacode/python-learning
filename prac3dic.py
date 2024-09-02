# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter marks in phy"))
marks.update({"phy": x})
y = int(input("Enter marks in chem"))
marks.update({"chem": y})
z = int(input("Enter marks in maths"))
marks.update({"maths": z})

print(marks)



