from concurrent.futures import ThreadPoolExecutor

import time

def print_num(number):
    time.sleep(1)
    return f"number is {number}"

numbers=[1,2,3,4,5]

with ThreadPoolExecutor(max_workers=3) as executor:
    results=executor.map(print_num,numbers)

for result in results:
    print(result)

#in thread pool executor , threads will be loosly coupled.

output:
number is 1
number is 2
number is 3
number is 4
number is 5
even with 1 sec sleep , we got answer in 1 second
