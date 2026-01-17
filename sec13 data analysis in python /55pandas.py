import pandas as pd
data=[1,2,4,4]
series=pd.Series(data)
print(series)
o/p-
0    1
1    2
2    4
3    4
dtype: int64


import pandas as pd
data=[1,2,4]
index=['a','b','c']
series=pd.Series(data,index=index)
print(series)
o/p-
a    1
b    2
c    4
dtype: int64


### DATA FRAMES
#data frame from dictionary of list

data={
    'name':["aarna","komal"],
    'age':[21,20],
    'city':['blr','chennai']
}

df=pd.DataFrame(data)
print(df)

o/p-
    name  age     city
0  aarna   21      blr
1  komal   20  chennai


df.head(5)
//read first 5 entries
df.tail(5) //this gives last 5 records

df['name'] //this will print all the rows of name
type(df['name']) -> this will be series

df.loc[0] -> pick first row
df.iloc[0] -> 1st index 
df.iloc[0][0] -> aarna



df

name	age
0	aarna	21
1	komal	30

print(df.at[1,'age']) -> 30
print(df.iat[1,1]) -> 30

df['salary']=[50000,60000]
	name	age	salary
0	aarna	21	50000
1	komal	30	60000

df.drop('salary',axis=1)
	name	age
0	aarna	21
1	komal	30


axis=1 means go and see column index 
axis=0 means go and see row index(default)

drop is temporary operation
salary will come back so we will put inplace=True

df.drop('salary',axis=1,inplace=True)

now salary is completely gone

df['age']=df['age']+1
everyones age will increase by 1




