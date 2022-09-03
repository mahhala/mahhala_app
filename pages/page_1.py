import streamlit as st
from PIL import Image
import datetime

code = '''
import streamlit as st
from PIL import Image

st.title('mahhala.app')
'''
st.code(code, language='python')

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
st.sidebar.write('コンディション：', condition)
    
start_date = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2022, 7, 1))
st.sidebar.write('Your birthday is:', start_date)

color = st.sidebar.color_picker('Pick A Color', '#00f900')
st.sidebar.write('The current color is', color)