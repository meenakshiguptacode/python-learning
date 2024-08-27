# tuples
# a built in data type that lets  create immutable sequence of values 
# tuples are immutable , which means once to have created it you can't change its values 
# its like strings
# Difference between list and tuple is list is mutable
# () will be used

tup = (2,6,7,8)
print(type(tup))
print(tup[0])
print(tup[1])
print(tup[1:3])


# tuple methods

# tup.index(el) 
# returns index of first occurrance
# tup.index(1) is 1

# tup.count(el)
# counts total occurance 
# tup.count(1) is 2

print(tup.index(6))
print(tup.count(6))
print(tup.count(8))
