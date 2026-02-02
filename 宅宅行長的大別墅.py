import streamlit as st
import time

st.set_page_config(page_title="宅宅行長的大別墅"
                   .layout="centered"`,page_icon=":house:")

st.title(" :green[歡迎來到宅宅行長的大別墅！]")
st.markdown("""這是宅宅行長的大別墅 :house:，宅宅行長家甚麼有喔!
            快來看看吧!""") 

if st.button("我要參觀一下"):
    with st.spinner('開門中...'):
        time.sleep(1.5)
    st.balloons()
    st.success("歡迎光臨！")



