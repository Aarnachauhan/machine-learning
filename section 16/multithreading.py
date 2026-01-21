import threading
import time

def print_num():
    for i in range(5):
        print(f"the number is {i}")
    

def print_letter():
    for letter in "ABCD":
        print(f"letter is{letter}")



t=time.time()
print_num()
print_letter()
finished=time.time()-t
print(finished)

output:
the number is 0
the number is 1
the number is 2
the number is 3
the number is 4
letter isA
letter isB
letter isC
letter isD
0.00055694580078125


---------------------------------------------
import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"the number is {i}")
    

def print_letter():
    for letter in "ABCD":
        time.sleep(2)
        print(f"letter is{letter}")



t=time.time()
print_num()
print_letter()
finished=time.time()-t
print(finished)

output:
the number is 0
the number is 1
the number is 2
the number is 3
the number is 4
letter isA
letter isB
letter isC
letter isD
18.00629496574402

//18 secs taken
-----------------------------------------------------------------
we can do concurrent execution
import threading
import time

def print_num():
    for i in range(5):
        time.sleep(2)
        print(f"the number is {i}")
    

def print_letter():
    for letter in "ABCD":
        time.sleep(2)
        print(f"letter is{letter}")

t1=threading.Thread(target=print_num)
t2=threading.Thread(target=print_letter)

t=time.time()

#start the thread
t1.start()
t2.start()

#wait for the threads to complete
t1.join()
t2.join()
#this will join both the threads to one
finished=time.time()-t
print(finished)


output:
PS C:\Users\asus\Documents\python\multithreading> python multi.py
the number is 0
letter isA
the number is 1
letter isB
the number is 2
letter isC
the number is 3
letter isD
the number is 4
10.00828218460083
(total time taken is almost half)
