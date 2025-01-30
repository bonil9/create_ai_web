import streamlit as st

# Streamlit 페이지 제목 설정
st.title("이지메이커 활용 과학 탐구실험 ")

# 링크 추가
chatgpt_url_1 = "https://blog.naver.com/sayment/223707256408"
chatgpt_url_2 = "https://blog.naver.com/sayment/223708052852"
chatgpt_url_21 = "https://blog.naver.com/sayment/223730744457"
chatgpt_url_3 = "https://blog.naver.com/sayment/223708447482"
chatgpt_url_4 = "https://blog.naver.com/sayment/223711052695"


st.markdown(f'[거리에 따른 복사평형 온도 확인 실험]({chatgpt_url_1})', unsafe_allow_html=True)
st.markdown(f'[열 전도 실험1]({chatgpt_url_2})', unsafe_allow_html=True)
st.markdown(f'[열 전도 실험2]({chatgpt_url_21})', unsafe_allow_html=True)
st.markdown(f'[손소독제 증발 실험]({chatgpt_url_3})', unsafe_allow_html=True)
st.markdown(f'[자유낙하 중력가속도 상수 측정 실험]({chatgpt_url_4})', unsafe_allow_html=True)
