# list is a built in data type that stores set of values 
# it can store elements of different types (integer , float , string etc etc )

# marks = [87, 64, 33, 94, 76]
# marks [0],marks [1]
# student = ["karan", 87, "Delhi"]

# assigment is alllowed in list
#marks[0] = 67
#len(marks)

marks = [87.9, 64.9, 33.7, 94.4, 76.6]
print(marks)
print(type(marks))

print(len(marks))
print(marks[0])

print(marks)
marks[0] =  90
print(marks)

# list slicing
# similar to string slicing 
# list_name[start_index: end_index] 
# ending index not included
 
 # marks = [87, 64, 33, 94, 76]
 # marks[1:4] = [87, 64, 33]
 # marks[-3:-1] = [33, 95]
 
print(marks[1:4])
print(marks[-3:-1])

# List methods
# list =  [69,6,44]


# list.append(4) - add one element at the end
#    [69,6,44,4]
# list.sort() - sorts in ascending order
#  [4,6,44,69]
# list.sort(reverse = TRUE) - sorts in descending order
#  [69,44,6,4]
# list.reverse() - reverse list
#  [4,44,6,69]
# list.insert(idx,el) - # insert element at index 


list = [56,78,667,677]
list.insert(1,5)
print(list)

print(list.remove(56))# remove first occurance of element
print(list.pop(1)) # remove element at index
print(list)
list.reverse()
print(list)



