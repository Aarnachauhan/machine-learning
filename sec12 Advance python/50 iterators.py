my_list=[1,2,3,4,5]
iterator=iter(my_list)

try:
    print(next(iterator))

except StopIteration:
    print("no more elemets left")

