import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("###  行事曆群組")
    st.radio("選擇群組", ["工作", "家庭"])

col_left, col_right = st.columns([1, 2], gap="large")
with col_left: 
    st.write("###  新增行程") 
    txt=st.text_input("時間:09:00")
    if st.button("新增行程"):
        @st.dialog("新增完成")
        def showadd():
            st.write("新增成功")
        showadd()
    today = st.date_input("選擇日期", datetime.date.today())
    meeting_time = st.time_input("選擇時間")
    my_color = st.color_picker("挑選辨識顏色","#1A73E8")


with col_right: 
    st.write("###  設定區") 
    tab1, tab2 = st.tabs(["本月行程", "已封存行程"])
    with tab1: 
        with st.container(border=True):
             with st.container(border=True):
                st.header("本月行程") 
        with tab2: 
            with st.container(border=True):
                st.header("已封存行程") 
        
