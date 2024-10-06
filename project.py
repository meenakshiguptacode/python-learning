import random

# def matchTarget(ranNum,num):
#     if(ranNum > num):
#         print("Try with high digit")
#     elif(ranNum < num):
#         print("Try with lower digit")
#     # elif(ranNum == num): 
#     #     print("its a match")
#     else:
#         print("its a match")

ranNum = random.randint(1,100)
print(ranNum)


# matchTarget(ranNum,num)



while True:
    num = int(input("Enter number between 1 to 100. Lets see if you are able to guess : "))
    if(ranNum == num):
        print("its a match")
        break
    elif(ranNum > num):
        print("Try with high digit")
    else:
        print("Try with lower digit")
    

print("game over")
    


