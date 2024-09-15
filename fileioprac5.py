# From a file containing numbers separated by comma, print the count of even numbers.



def countEvenNumber():
    count = 0
    with open("numberfile.txt","r") as f:
        data = f.read()
        result = data.split(",")  
        print(result)  
        for el in result:
            if(int(el) % 2 == 0):
                count = count + 1
        print(count)
        return
        
        
        
countEvenNumber()
