###function copy

#function copy
def welcome():
    return "welcome to the advance python course"

welcome()
o/p- welcome to the advance python course

wel=welcome
wel()
o/p- welcome to the advance python course


del welcome
wel()
o/p - welcome to the advance python course


#closure - function inside function
def main_welcome():
    msg="hello"
    def sub_welcome():
        print("this is sub welcome function")
        print(msg)
        print("bye")

    return sub_welcome()

main_welcome()

o/p
this is sub welcome function
hello
bye


#passed function inside a function
def main_welcome(func,lst):
    msg="hello"
    def sub_welcome():
        print("this is sub welcome function")
        print(func(lst))
        print("bye")

    return sub_welcome()


main_welcome(len,[1,2,3])


o/p-
this is sub welcome function
3
bye


#decorator
def main_welcome(func):
    msg="hello"
    def sub_welcome():
        print("this is sub welcome function")
        func()
        print("bye")

    return sub_welcome()

def course():
    print("this is course intro")


    return course
main_welcome(course)

o/p 
this is sub welcome function
this is course intro
bye


@main_welcome
def course():
    print("this is course intro")

o/p 
this is sub welcome function
this is course intro
bye

whenever we write main_welcome as a decorator , this course func will go inside main welcome as a parameter



