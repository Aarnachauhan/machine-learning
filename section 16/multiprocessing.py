import multiprocessing
import time

def square():
    for i in range(1,6):
        time.sleep(1)
        print(f"square is {i*i}")


def cube():
    for i in range(1,6):
        time.sleep(1.5)
        print(f"cube is {i*i*i}")


if __name__== '__main__':
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)

    t=time.time()
    #start the process
    p1.start()
    p2.start()

    #wait for the process

    p1.join()
    p2.join()
    finished=time.time()-t

    print(finished)

output:
PS C:\Users\asus\Documents\python\multithreading> python multiprocess.py
square is 1
cube is 1
square is 4
square is 9
cube is 8
square is 16
cube is 27
square is 25
cube is 64
cube is 125
7.664434432983398
