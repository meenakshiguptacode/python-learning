# Write a recursive function to print all elements in a list.
# Hint : us

# A
# e list & index as parameters.


def printItemInList(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    printItemInList(list, idx+1)
    
    
    
    
    
    
list = ["a","b","c","d"]
printItemInList(list, 3)    


printItemInList(list, 0)    

    
    