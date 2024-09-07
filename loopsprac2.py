# WAP to find the factorial of first n numbers. (using for)




n = int(input("enter number for factorial"))
fac = 1
for el in range(1,n+1,1):
    fac = fac * el
print(fac)