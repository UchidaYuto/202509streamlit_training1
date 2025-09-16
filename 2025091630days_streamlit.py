import pandas as pd
import numpy as np
#import plotly.graph_objects as go
#import plotly.express as px
import streamlit as st
import altair as alt
from datetime import time, datetime

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

#day8 スライダーの練習
#st.slider練習
st.header('st.slider')

#例1
st.subheader('Slider') #スライダー

age = st.slider('How old are you?', 0 , 130, 25) #st.slider(表示名, 最小値, 最大値, 初期値)
st.write("I'm", age, 'years pld') #print文的な


#例2
st.subheader('Range slider') #範囲スライダー

values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)) #うん？表示名,最小, 最大, タプル(下限,上限)
st.write('Values:', values)

#例3
st.subheader('Range time slider') #範囲時間スライダー

appointment = st.slider(
    "Schedule your appointment:",
    value=(time(11, 30), time(12, 45))) #表示名, value(下限11時30分, 上限12時45分)
st.write("You're scheduled for:", appointment)

#例4
st.subheader('Datetime slider') #日時スライダー

start_time = st.slider(
    "When do you start?",
    value=datetime(2020,1,1,9,30), #2020年1月1日9時30分
    format="MM/DD/YY - hh:mm") #表示名, 初期値, フォーマット
st.write("Start time:", start_time)

#day9 折れ線グラフ表示
st.header('Line chart')

chart_data = pd.DataFrame(
    np.random.randn(20, 3), #20行3列のランダムな数値
    columns=['a', 'b', 'c']) #列名

st.line_chart(chart_data) #折れ線グラフ表示 20行分の3列データを折れ線グラフで表示


#day10 選択ウィジェット
'''
ユーザーに好きな色を尋ねるシンプルなアプリ
1. ユーザーが色を選択
2. アプリから選択された色が出力される
'''
st.header('st.selectbox')

option = st.selectbox(
    'What is your favorite color?', #表示名
    ('Blue', 'Red', 'Green')) #選択肢

st.write('Your favorite color is', option)

