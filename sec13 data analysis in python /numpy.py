NUMPY

import numpy as np
a=np.array([1,2,3])
a.shape

O/P - (3,)
if 1 no is there than it is 1 D array


a1=np.array([[1,2,3]]) //2d array as we have 2 brackets
a1.shape
o/p - (1,3)
1 row 3 coloum 


np.arange(0,10,2)
o/p 
array([0, 2, 4, 6, 8])

np.arange(0,10,2).reshape(5,1)
o/p:
array([[0],
       [2],
       [4],
       [6],
       [8]])

np.ones(3,4)
3 rows with 4 columns and their element is 1

np.eye(3) #identity matrix



#vectorization maths
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])

print("add" , v1+v2)
print("sub" , v1-v2)
same for mul and div(/)



arr1=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.mean(arr1))
print(np.std(arr1))
print(np.median(arr1))
print(np.var(arr1))

o/p
5.0
2.581988897471611
5.0
6.666666666666667

data=np.array([1,2,3])
data[data>1]
o/p
array([2,3])



