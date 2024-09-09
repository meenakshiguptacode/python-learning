# functions 
# block of statement that performs some specific task

# def fun(parm1 , parm 2)
# some work
# return val

# func call
# fun(parm1 , parm 2)

# func definition
def sum(a,b): # parameters
    s = a + b
    return s 

print(sum(2,3)) # func call ; arugements



def print_hello():
    print("hello")

output = sum(2,3)
print(output) # none



# there are 2 types 0f func in python

# built in func 
 # print()
 # len()
 # type()
 # range()
 
 
# user defined func 
# written by user


# default parameter
# assigning  default value to parameter which is used when no parameter is passed

 
def cal_prod(a =1 , b =2):
    print(a*b)
    return a * b

cal_prod()