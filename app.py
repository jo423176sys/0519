import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組",["學生","老師","家長"],True)

col_left, col_right = st.columns([1, 1], gap="large")
with col_left: 
    st.write("###  新增行程") 
    txt=st.text_input("行程主旨")
    my_color = st.color_picker("挑選辨識顏色","#1A73E8")

with col_right: 
    st.write("###  設定區") 
    today = st.date_input("選擇日期", datetime.date.today())
    meeting_time = st.time_input("選擇時間")

view = st.segmented_control(
  "檢視模式",
  ["月視角", "週視角"],
  default="月視角"
)
    
tag = st.pills(
  "行程屬性",
  ["#工作", "#家庭", "#緊急"]
)
