# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]


nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

idx = 0
x = int(input("Enter the number you want to find "))
for val in nums:
    idx += 1
    if(x == val):
        print("Number found at index" , idx)
        
        break
        
else:
    print("not found")