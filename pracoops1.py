# Create student class that takes name & marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.


class Student:
    


    # parameterized contructor
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in second database")

    def get_marks_avg(self):
        avg = sum(self.marks)/len(self.marks)
        return avg
    
    
    
    
s1 = Student("karan",[98,90,96])
print(s1.name,s1.marks)

print(s1.get_marks_avg())