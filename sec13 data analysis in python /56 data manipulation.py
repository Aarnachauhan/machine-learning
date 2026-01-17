
df.isnull()  #this will give false where there is valyse and true where there is no value

df.isnull().any()
Age                        False
Sex                        False
Chest pain type            False
BP                         False
Cholesterol                False
FBS over 120               False
EKG results                False
Max HR                     False
Exercise angina            False
ST depression              False
Slope of ST                False
Number of vessels fluro    False
Thallium                   False
Heart Disease              False
dtype: bool

no missing value found , if there is a missing value toh uder true ata
----------------------------------------------------------------------------
df.isnull().sum()
Age                        0
Sex                        0
Chest pain type            0
BP                         0
Cholesterol                0
FBS over 120               0
EKG results                0
Max HR                     0
Exercise angina            0
ST depression              0
Slope of ST                0
Number of vessels fluro    0
Thallium                   0
Heart Disease              0
dtype: int64

no missing value 

---------------------------------------------------------------------------------------

df.fillna(0) -> where ever there is missing value , fill it with 0 
df['Sex_fillna']=df['Sex'].fillna(df['Sex'].mean())
-> in df['Sex']-> wherever there is missing value , fill it with mean

-----------------------------------------------------------------------------------
df=df.rename(columns={'Sex':'Gender'}) -> this will change Sex to Gender 
we have to give it in key value pair

--------------------------------------------------------------------------------
df['MAX_HR']=df['MAX HR'].astype(float)
change the datatype

------------------------------------------------------------------------------------------
df['new age']=df['Age'].apply(lambda x:x*2)
df

new age column will be made and then it will have 2*old age
------------------------------------------------------------------------------------
##multiple aggregate function
df.groupby('Age')['new age'].agg(['mean','count','sum'])

	mean	count	sum
Age			
29	58.0	1	58
34	68.0	2	136
35	70.0	3	210
37	74.0	2	148
38	76.0	1	76
39	78.0	3	234
40	80.0	3	240
41	82.0	9	738
42	84.0	8	672
43	86.0	7	602
44	88.0	10	880
45	90.0	7	630
46	92.0	7	644
47	94.0	4	376
48	96.0	7	672
49	98.0	5	490
50	100.0	7	700
51	102.0	12	1224
52	104.0	11	1144
53	106.0	7	742
54	108.0	16	1728
-------------------------------------------------------------------
df=pd.DataFrame({'Key':['A','B','C'], 'Value1':[1,2,3]})
df2=pd.DataFrame({'Key':['A','B','D'] , 'Value2':[5,6,7]})

df2
	Key	Value2
0	A	5
1	B	6
2	D	7

dfd
	Key	Value1
0	A	1
1	B	2
2	C	3


pd.merge(df,df2,on='Key',how="inner")

Key	Value1	Value2
0	A	1	5
1	B	2	6


pd.merge(df,df2,on='key' , how='outer')
	Key	Value1	Value2
0	A	1.0	5.0
1	B	2.0	6.0
2	C	3.0	NaN
3	D	NaN	7.0

same for left and right

