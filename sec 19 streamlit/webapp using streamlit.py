import streamlit as st
import pandas as pd
import numpy as np

st.title("hello streamlit")

st.write("this is a simple text")

#create a simple dataframe

df= pd.DataFrame ({
    'first-col' : [1,2,3,4],
    'second-col': [5,3,5,7]
})

st.write("this is the dataframe")
st.write(df)


#create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','b','c'] 
    #20 rows and 3 columns 
)

st.line_chart(chart_data)

--------------------------------------------
import streamlit as st

st.title("streamlit text input")

name=st.text_input("enter your name")

if name:
    st.write(f"hello {name}")

age=st.slider("select your age",0,100,25)
st.write(f"your age {age}")
-------------------------------

selection


options=['c++','java','javascript','python']
choice=st.selectbox("choose your favourite",options)
st.write(f"you selected {choice}")
-------------------------------------------------
#upload a file
import pandas as pd



uploaded_file=st.file_uploader("choose a csv file ", type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)

------------------------------------------------------


---------------------------------------------
