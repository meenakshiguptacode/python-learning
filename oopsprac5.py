class Order:
    
    # parameterized contructor
    def __init__(self,item,price):
        self.item = item
        self.price = price
    # a > b
    
    def __gt__(self,odr2):
        return self.price > odr2.price





order1 = Order("chip",20)
order2 = Order("coffee",120)


print(order1 > order2)
