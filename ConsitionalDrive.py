# nesting
age = int(input("Enter age:"))

if(age >= 18):
    if(age >= 80):
       print("can not  drive")
    else:
       print("can drive")
else:
    print("can not drive")