import streamlit as st

# Streamlit 페이지 제목 설정
st.title("MBL(과학실험)+스파이크프라임")

# 링크 추가
chatgpt_url_1 = "https://blog.naver.com/sayment/223619778211"
chatgpt_url_2 = "https://blog.naver.com/sayment/223620545080"


st.markdown(f'[등속도 운동 실험]({chatgpt_url_1})', unsafe_allow_html=True)
st.markdown(f'[등가속도 운동 실험]({chatgpt_url_2})', unsafe_allow_html=True)
