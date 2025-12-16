

age=20
height=160.1
name="aarna"

# printing 
print("age", age)
print("height" , height )
print("name", name)

variables should start with letters or _ and contain letters . no other special characters
can contains numbers in between

invalid variable names
3name
first-name
haaer@

python is case sensitive 
python is dynamically typed


age=40 //age converted into string and we can do vise versa 
print(type(age))
age_str=str(age)
print(age_str)
print(type(age_str))

o/p -
<class 'int'>
40
<class 'str'>

age='40'
int(age)
this will be converted but not 
name="aarna"
int(name) //this cant be converted into int .


asking for input 
age=input("what is your age")
print(age, type(age))

we can also convert it into int 
age=int(input("what is your age"))
print(age, type(age))


