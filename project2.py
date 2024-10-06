# random password generator


import random
import string

# print(string.ascii_letters)
# print(string.digits)
# print(string.punctuation)

itemList = string.ascii_letters + string.digits + string.punctuation
# password = ""
pass_len = 12


# list comprehension [func for i in range(n)]

res = "".join([random.choice(itemList) for i in range(pass_len)])

print(res)
 





# for i in range(pass_len):
#     password += random.choice(itemList)
#     i + 1
    

#print(password)