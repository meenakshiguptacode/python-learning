#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
# [1, 2, 3, 2, 1] [1, “abc”, “abc”, 1]

list1 = [1,2,1]
list2 = [1,2,3]


copy_list1 = list2.copy()
copy_list1.reverse()

if(copy_list1 == list2):
    print("List is palindrome")
else:
    print("List is not palindrome")






copy_list2 = list1.copy()

