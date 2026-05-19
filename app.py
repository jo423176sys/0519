import streamlit as st
st.set_page_config(page_title="微型 TimeTree", layout="wide")
with st.sidebar:
    st.write("###  行事曆群組")
    
col_left, col_right = st.columns([1, 3], gap="large")
with col_left: 
    st.write("###  新增行程") 

with col_right: 
    st.write("###  設定區") 
    with st.container(border=True): 
    tab1, tab2 = st.tabs(["本月行程", "已封存行程"])
    with tab1: 
        st.header("本月") 
        st.write("本月")
    with tab2: 
        st.header("已封存") 
        st.write("已封存")
    
