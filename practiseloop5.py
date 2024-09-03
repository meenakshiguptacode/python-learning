# Search for a number x in this tuple using loop:

# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = int(input("Enter number you want to find "))
numTuple = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
i = 0 


while  i < len(numTuple):
    if(num == numTuple[i]):
        print("Match found at", i+1 , "position")
    i += 1