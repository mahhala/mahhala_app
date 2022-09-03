import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# データ分析関連
df = pd.read_csv('./data/data.csv', index_col='月', encoding = 'shift-jis')
# st.table(df)
st.line_chart(df)
st.bar_chart(df)

# matplotlib
fig, ax = plt.subplots()
ax.plot(df.index, df['最高気温(℃)'])
ax.set_title('matplotlib graph')
st.pyplot(fig)

condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
st.sidebar.write('コンディション：', condition)
    
start_date = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2022, 7, 1))
st.sidebar.write('Your birthday is:', start_date)

color = st.sidebar.color_picker('Pick A Color', '#00f900')
st.sidebar.write('The current color is', color)