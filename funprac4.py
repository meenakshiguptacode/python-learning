# WAF to find the factorial of n. (n is the parameter)



def print_fact(num):
    fac = 1
    for el in range(1,num+1,1):
        fac = fac * el
        print(el)
    return fac
    
           
        
    
n = int(input("Enter number for factorial   "))
fac = print_fact(n)
print(fac)