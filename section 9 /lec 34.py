#read file 
with open('example.txt',mode='r') as file:
    content=file.read()
    print(content)

whatever will be in file will come here

#this is to read whole file line by line 
with open('example.txt','r') as file:
    for line in file:
        print(line)

#to remove newline space/ newline charactor .
  with open('example.txt','r') as file:
    for line in file:
        print(line.strip())


#to rewrite the file - everything will go away and only hello world will be written in example.txt
with open('example.txt','w') as file:
    file.write("hello world\n")


'a' -> this is append 
at the end it will be added





        
