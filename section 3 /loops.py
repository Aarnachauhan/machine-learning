range(5)
this will generate no from 0 to 5

for i in range(5):
  print(i)
0/p = 0 1 2 3 4 

##for loop
for i in range(1,6):
    print(i)
  o/p 1 2 3 4 5 

range(start, stop before , step)
range(1,10,1) -> 1 to 9

range(10,1,-2) = 10 , 8  ... 2

str="aarna chauh"
for i in str:
  print(i)

a
a
r
n
a

c
h
a
u
h

cnt=0
while cnt<5:
    print(cnt)
    cnt=cnt+1


loop control statements
1) break
2) continue 

for i in range(10):
    if i==5:
        break
    print(i)

0 to 4 , break will let us go out of for loop

continue - skips current statement and continues with next iterations
print odd numbers
for i in range(10):
    if i%2==0:
        continue
    print(i)

1,3,5,7,9

pass - is a null operation and it does nothing
for i in range(10):
    if i%2==0:
        pass
    print(i)
0 to 9

nested loops- a loop inside a loop 
for i in range(3):
    for j in range(2):
        print(f"i:{i} and j: {j}" )

i:0 and j: 0
i:0 and j: 1
i:1 and j: 0
i:1 and j: 1
i:2 and j: 0
i:2 and j: 1


