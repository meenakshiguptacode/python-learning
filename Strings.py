str1 = "This is string"
str2 = 'Meenakshi'
str3 = """this is a string \n we are just testing escspe chsracter  dddd"""

print(str3)

len = len(str3);
final_str = str1 + "  " + str2;
print(final_str)

str = "Meenakshi college"
ch =  str[0]
print(ch)

print(str[:4]) #[0:4]
print(str[5:]) #[5:len(str)]

# string operations 
str = "i am studying strings from youtube"

print(str.endswith("tube"))

print(str.capitalize())
print(str.replace("o","a"))
print(str.find("ou"))
print(str.count("be"))