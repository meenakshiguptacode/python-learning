# break and continue

# break
# used to terminate the loop when encountered 

# continue
# terminates execution in the current iteration & continues execution of loop with the next iteration 


i = 1 
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("loop eneded")       



j = 1
while j <= 5:
    if(j == 3): 
        j += 1
        continue
    print(j)
    j += 1
    