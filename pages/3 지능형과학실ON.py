import streamlit as st

# Streamlit 페이지 제목 설정
st.title(" 지능형 과학실 ON  ")

# 링크 추가
chatgpt_url_1 = "https://blog.naver.com/sayment/223637285124"
chatgpt_url_2 = "https://blog.naver.com/sayment/223675587691"
chatgpt_url_3 = "https://blog.naver.com/sayment/223726624617"


st.markdown(f'[학교 관리자 권한 받기!!]({chatgpt_url_1})', unsafe_allow_html=True)
st.markdown(f'[지능형과학실ON 사용중 당황하게 만드는 것들]({chatgpt_url_2})', unsafe_allow_html=True)
st.markdown(f'[협력탐구로 설정 해야하는 경우]({chatgpt_url_3})', unsafe_allow_html=True)

