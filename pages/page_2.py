import streamlit as st
from PIL import Image
import datetime

with st.form(key='profile_form'):
    # テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    # セレクトボクス
    age_category_1 = st.selectbox(
        '性別',
        ('男性(MALE)', '女性(WOMAN)'))
    age_category_2 = st.radio(
        '年齢層',
        ('子ども(１８才未満)', '大人(１８才以上)'))

    hobby = st.multiselect(
        '趣味',
    ('スポーツ', '読書', 'プログラミング', 'アニメ・映画', '釣り', '料理'))

    # ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')
    if submit_btn:
        st.text(f'いらっしゃい！{name}さん！{address}に送っておいたよ〜！')
        st.text(f'性別: {age_category_1}')
        st.text(f'年齢層: {age_category_2}')
        st.text(f'趣味: {", ".join(hobby)}')
        
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)
st.sidebar.write('コンディション：', condition)
    
start_date = st.sidebar.date_input(
     "When's your birthday",
     datetime.date(2022, 7, 1))
st.sidebar.write('Your birthday is:', start_date)

color = st.sidebar.color_picker('Pick A Color', '#00f900')
st.sidebar.write('The current color is', color)