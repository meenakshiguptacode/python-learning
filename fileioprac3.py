#Search if the word “Unique” exists in the file or not.


with open("practice.txt","r") as f:
    data = f.read()
    if(data.find("Unique") != 1):
        print("Word match")
    else:
        print("Word does not match")
        