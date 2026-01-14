#read file 
with open('example.txt',mode='r') as file:
    content=file.read()
    print(content)

whatever will be in file will come here

#this is to read whole file line by line 
with open('example.txt','r') as file:
    for line in file:
        print(line)

#to remove newline space .
  with open('example.txt','r') as file:
    for line in file:
        print(line.strip())



        
