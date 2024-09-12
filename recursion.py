# Recursion 

# when a func calls itself repeatedly

# print  to 1 backwards 

def show(n):
    if(n == 0): # base case
        return
    print(n)
    show(n-1)
    
    
def fact(n):
    if(n == 0 or n == 1): # base case
        return 1
    else:
        return n * fact(n -1)
    
    

    
num = int(input("Enter number : "))
show(num)

factnum = fact(num)
print(factnum)

