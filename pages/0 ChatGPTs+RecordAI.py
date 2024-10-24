import streamlit as st

# Streamlit 페이지 제목 설정
st.title("ChatGPTs + RecordAI")

# 링크 추가
chatgpt_url_1 = "https://chatgpt.com/g/g-PeGH8Y8Mi-hagsaengbu-saenggibu-jagseonghaedeuryeoyo-haengbal-seteug-dongari-seupoceukeulreob-jayuhaggi-jayul-codeung-junghaggyo-godeunghaggyo"
chatgpt_url_2 = "https://chatgpt.com/g/g-MFJnyFAFQ-siheommunje-danweonpyeongga-siheomculje-gosaculje-gyosa"
chatgpt_url_3 = "https://chatgpt.com/g/g-9N4SjezVJ-self-introduction-writing-recruitment"

st.markdown(f'[생기부 작성 ChatGPTs 보러 가기]({chatgpt_url_1})', unsafe_allow_html=True)
st.markdown(f'[시험 출제 ChatGPTs 보러 가기]({chatgpt_url_2})', unsafe_allow_html=True)
st.markdown(f'[영어 자기소개서 보러 가기]({chatgpt_url_3})', unsafe_allow_html=True)
