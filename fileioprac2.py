# WAF that replace all occurrences of “Gifts” with "presents" in practice.txt file.


with open("practice.txt","r") as f:
    data = f.read()
    new_data = data.replace("Gifts","presents")
    print(new_data)


with open("practice.txt","w") as f:
    f.write(new_data)