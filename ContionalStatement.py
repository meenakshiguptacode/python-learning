# if-elif-else(syntax)
# light = input("light: ")
# if(light == "red"):
#     print("stop")
# elif(light == "yellow"):
#     print("look")
# elif(light == "green"):
#     print("go")
# else:
#     print("light is broken")
    
    
    
    
# Contidional statement
# single line if or ternary operator 

# <var> = <val1> if <condition> else <val2> 
# food = input("food:")
# eat = "yes" if food == "cake" else "no"
# print(eat)


# <stt1> if <condition> else <stt2>

food = input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")


# clever if/ ternanry operator
#<var> = (false_val, true_val) [<condition>]

age = int (input("age: "))
vote = ("yes", "no") [age < 18]
print(vote)

sal = float(input("salary:"))
tax = sal * (0.1 , 0.2) [sal <= 50000]
print(tax)







 