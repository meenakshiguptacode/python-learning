# __init__ func

# contructor 
# all classes have a func called __init__() , which is always executed when class is being initiated


# creating class 

class Student:
    
    # class attr 
    college_name = "CVB College"
    name = "test"
    # default contructors
    def __init__(self):
       print("Adding new student in database")

    # parameterized contructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in second database")
        
    def welcome(self):
        print("Hello, students", self.name)
        
    def get_marks(self):
        return self.marks
        
# creating object

s1 = Student("karan",98)
print(s1.name,s1.marks)
print(s1.college_name)

# the self parameter is a reference to the current instance of the class and is used to access variable that belongs to the class



s2 = Student("karanra",90)
print(s2.name,s1.marks)


# class and intance attribute

# Class.attr
# obj.attr


# name and marks are  intance attribute as it is different for everyone
# we generally use self with that


# if something is common then we make it class attr eg eg college name will be same for all Student
# This will ocuppy space only one time unlike intance attribute 


# if we have same name in  class and intance attribute then intance attribute takesp precedence
# obj attr > class attr



# methods 

# methods are the func that belongs to the object

# creating class

# class Student:
#     def __init__(self,name):
#         self.name = name
    
#     def hello(self):
#         print("hello",self.name)
        
        
# # creating object

# s1 = Student("karan")
# s1.hello()

s2.welcome()
print(s2.get_marks())



