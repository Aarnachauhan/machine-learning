import matplotlib.pyplot as mt
x=[1,2,3]
y=[1,4,9]
mt.plot(x,y)
mt.xlabel('X AXIS')
mt.ylabel('Y AXIS')
mt.title('BASIC LINE PLOT')

---------------------------------------------------------------------
mt.plot(x,y,color='red',linestyle='--',marker='o')

------------------------------------------------------------------------
data=[1,1,2,3,3,4,4,4,5,5]
mt.hist(data,bins=5,color='orange')
o/p
(array([2., 1., 2., 3., 2.]),
 array([1. , 1.8, 2.6, 3.4, 4.2, 5. ]),
 <BarContainer object of 5 artists>)
--------------------------------------------------------------------------
