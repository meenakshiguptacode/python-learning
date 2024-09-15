# WAF to find in which line of the file does the word "Items" occur first.
# Print -1 if word not found.



def checkForLine():
    word = "Itemsff"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
    return -1


print(checkForLine())