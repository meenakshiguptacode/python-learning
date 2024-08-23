# String is the data type that store sequence of characters 
# Basic operations
# - Concatnation
# "hello" + "world" -> "helloworld"
# length of str
# len(str) 


str1 = "This is string"
str2 = 'Meenakshi'
str3 = """this is a string \n we are just testing escspe chsracter  dddd"""

#print(str3)

len1 = len(str3);
final_str = str1 + "  " + str2;
#print(final_str)
#print(len(final_str))

str1 = "new"
str2 = "code"
#print(str1 + " " + str2)

# indexing 
# assigment is not possible in index
# str[4] = "Q" (not possible)

str = "Meenakshi college"
ch =  str[0]
#print(ch)

# slicing
# acessing parts of string
# str[starting_idx : ending_idx ] #ending idx is not included
print(str[0:4])
print(str[1:4])
print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

# string operations 
str = "i am studying strings from youtube"

print(str.endswith("tube"))

print(str.capitalize())
print(str.replace("o","a"))
print(str.find("ou"))
print(str.count("be"))

# slicing
# negative index
# Apple
# -5 -4 -3 -2 -1

strtest = "joypoy"
print(strtest[ -3 : -1])
