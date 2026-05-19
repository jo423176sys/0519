import streamlit as st
import datetime

st.set_page_config(page_title="微型 TimeTree", layout="wide")

# 群組選擇
mode = st.radio(
    "選擇群組",
    ["學生", "老師", "家長會", "校友會"],
    horizontal=True
)

# 初始化
if "mylist" not in st.session_state:
    st.session_state.mylist = []

l, r = st.columns(2)

# 左側：新增行程
with l:
    t1 = st.text_input("行程主旨")
    t3 = st.date_input("日期選擇", datetime.date.today())
    t4 = st.time_input("時間選擇")

    n1 = st.number_input(
        "行程開始前幾分鐘提醒？",
        min_value=0,
        max_value=60,
        value=15
    )

    if st.button("新增行程"):

        # 用 dictionary 儲存
        st.session_state.mylist.append({
            "群組": mode,
            "主旨": t1,
            "日期": t3,
            "時間": t4,
            "提醒": n1
        })

# 右側：顯示行程
with r:

    # 分群顯示
    groups = ["學生", "老師", "家長會", "校友會"]

    for g in groups:

        st.subheader(f"{g} 行程")

        found = False

        for item in st.session_state.mylist:

            if item["群組"] == g:

                found = True

                with st.container(border=True):
                    st.write(f"行程主旨：{item['主旨']}")
                    st.write(f"日期：{item['日期']}")
                    st.write(f"時間：{item['時間']}")
                    st.write(f"提醒：{item['提醒']} 分鐘前")

        if not found:
            st.info("目前沒有行程")
