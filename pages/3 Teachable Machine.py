import streamlit as st

# Streamlit 페이지 제목 설정
st.title("Teachable Machine")

# 링크 추가
teachable_url = "https://teachablemachine.withgoogle.com/models/g3vwr8jds/"

st.markdown(f'[성운 구별하기 모델 보러 가기]({teachable_url})', unsafe_allow_html=True)
