import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")
mode = st.radio("選擇群組",["學生","老師","家長"],horizontal=True)

col_left, col_right = st.columns([1, 1], gap="large")
with col_left: 
    st.text_input("行程主旨")
    my_color = st.color_picker("顏色設定")

with col_right: 
    st.date_input("選擇日期", datetime.date.today())
    st.time_input("選擇時間")
    
with st.popover("快速進階篩選"):
    st.checkbox("隱藏已過期行程")
    
view = st.segmented_control(
  "檢視模式",
  ["月視角", "週視角"],
  default="月視角"
)
    
tag = st.pills(
  "行程屬性",
  ["#工作", "#家庭", "#緊急"]
)

is_open = st.toggle(
  "開啟 24H 郵件自動發信通知",
  value=True
)
