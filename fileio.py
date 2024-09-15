# file i/o in python 

# python an be used to preform operations in a file 
# (read and write data)


# type of all files 
# 1. text files: .txt , .docx , .log etc 

# 2. binary files: .mp4 ,.mov, .png , .jpeg etc 


# open , read & close file

# we ave to open a file before reading or writing 
 
 
# f = open("file_name", "mode")

# mode : 
# r : read mode 
# w : write mode


# data = f.read()
# f.close()


# Reading a file

# data = f.readline( ) #reads one line at a time
# data = f.read( ) #reads entire file


f = open("demo.txt", "r")
#data = f.read()

dataline = f.read(100)
datalinek = f.readline()
#print(data)
#print(dataline)
print(datalinek)
#print(type(data))
f.close()

# Writing to a file

# f.write( “this is a new line“ )
# f = open( “demo.txt”
# ,
# “w”)

# #overwrites the entire file

# f.write( “this is a new line“ ) #adds to the file




f = open("demo.txt", "w")

f.write("Traditional Values: Respect for elders, family unity, and the importance of marriage are deeply ingrained in Indian culture.")


f.write("\n After that nodejs")

f.close()




g = open("demotest.txt", "w")
g.write("test")
g.close()
