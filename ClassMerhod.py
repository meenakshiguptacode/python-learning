# class method

# class method is bound  to the class nd recives the class as on implicit first argument

#  note: static method can't access or modify class  state and generally for utility

# class Student:
    # @classmethod # decorator
    # def college(cls)
    #     pass
    
    
class Person:
    name = "anon"
    
    # def changeName(self, name):
    #     self.__class__.name = "Rahul"
    #     # self.__class__. Person.
        
    # Better way to do this is below
    
    @classmethod
    def changeName(cls,name):
        cls.name = name        

p1 = Person()
p1.changeName("Rahul Kumar")
print(p1.name)
print(Person.name)


