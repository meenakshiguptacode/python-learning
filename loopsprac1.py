# WAP to find the sum of first n numbers. (using while)



n = int(input("enter numbetd for sum"))
sum = 0
i = 0; 
while  i <= n:
    sum = sum + i
    i += 1

print(sum)