# Write a recursive function to calculate the sum of first n natural numbers.


def sumOfNum(n):
    if(n == 0): # base case
        return 0
    return n + sumOfNum(n - 1)
    
    

    
num = int(input("Enter number : "))
sumnum = sumOfNum(num)

print(sumnum)