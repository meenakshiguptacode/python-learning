# Super method

# super() method is used to access methods of the parent class

class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("Car started")   
        
    @staticmethod
    def stop():
        print("Car sttopped")      
    

class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.brand = name
        super().start()
        
        


# car1 = ToyotaCar("creta")
    
# car2 = ToyotaCar("Kia")


# print(car1.start())

# print(car2.stop())

# car1 = Fortuner("diesel")
# car1.start()

car1 = ToyotaCar("prius","electric")
print(car1.type)

