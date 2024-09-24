# inheritance
# when one class (child/derived) dervies the properties and method of another class (parents)


# Class Car:
#     ...


# Class ToyotaCar(Car):
#     ...


# Types of inhertance

# 1. Single inhertance
# 2. Mutli level inhertance
# 3. multpile inheritance



class Car:
    @staticmethod
    def start():
        print("Car started")   
        
    @staticmethod
    def stop():
        print("Car sttopped")      
    

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand
        

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
        

# car1 = ToyotaCar("creta")
    
# car2 = ToyotaCar("Kia")


# print(car1.start())

# print(car2.stop())

car1 = Fortuner("diesel")
car1.start()