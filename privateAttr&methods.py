# private (like) attribute and methods

# private attribute and methods  are meant to be used only within the class and are not aaccessible from outside the class



# __name


class Person: 
    
    def __hello(self):
        print("hello")
        
    def welcome(self):
        self.__hello()
    
    
p1 = Person()


## this will give error as we trying to access private variable
p1.welcome()