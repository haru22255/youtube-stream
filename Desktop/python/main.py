import streamlit as st
import numpy as np
import pandas as pd 
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('プログレスーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'iteration {i+1}')
    bar.progress(i +1)
    time.sleep(0.1)

'Done!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if  button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

#text = st.text_input('あなたの今の趣味を教えて下さい。')
#condition = st.slider('あなたの今の調子は？', 0 ,100,50)

#if st.checkbox('Show Image'):
#   img = Image.open('sample.jpg')
#   st.image (img , caption='空', use_column_width = True)
