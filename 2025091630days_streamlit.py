import pandas as pd
import numpy as np
#import plotly.graph_objects as go
#import plotly.express as px
import streamlit as st
import altair as alt
#from datetime import datetime

st.write('Hello world!')

st.header('st.button')
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')

# day5
st.header('st.write')

st.write('Hello, *world!* :sunglasses:') #*斜体*, :マークダウン(絵文字):

st.write(1234)

df = pd.DataFrame({
    'first column' : [1,2,3,4],
    'second column': [10, 20 ,30 , 40]
})

st.write('Below is a DataFrame:', df, 'Above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)