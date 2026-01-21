from concurrent.futures import ProcessPoolExecutor
import time

def print_num(number):
    time.sleep(1)
    return f"number is {number}"

numbers=[1,2,3,4,5]
if __name__=="__main__":

    with ProcessPoolExecutor(max_workers=3) as executor:
        results=executor.map(print_num,numbers)

    for result in results:
        print(result)

output:
number is 1
number is 2
number is 3
number is 4
number is 5


in 1 second
