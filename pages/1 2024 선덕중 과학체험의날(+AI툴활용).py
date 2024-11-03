import streamlit as st

# 페이지 구성 설정을 위한 스타일링 적용
st.markdown(
    """
    <style>
    .title {
        font-size: 2em;
        text-align: center;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 사용자 정의 스타일이 적용된 타이틀 텍스트
st.markdown('<div class="title">2024 선덕중학교 과학 체험의 날 행사(AI툴 사용)</div>', unsafe_allow_html=True)

# 링크 추가
chatgpt_url_1 = "https://blog.naver.com/sayment/223413856862"
chatgpt_url_2 = "https://docs.google.com/forms/d/e/1FAIpQLSdAV2tktVKqzXciNTnDTEoxRL3TvDzwkGCWkWCzayQ__yXcQA/viewform?vc=0&c=0&w=1&flr=0"
chatgpt_url_3 = "https://drive.google.com/drive/folders/1lwmcCjBvliK5XGpUvkhBhUNIK9KgD2RF?usp=sharing"

st.markdown(f'[행사 전체 적인 내용(필독)]({chatgpt_url_1})', unsafe_allow_html=True)
st.markdown(f'[실제 체험해보기]({chatgpt_url_2})', unsafe_allow_html=True)
st.markdown(f'[다른학교에서도 시도해보시라고 공유폴더(꼭 꼭 사본 만드시고, 사본을 수정하세요)]({chatgpt_url_3})', unsafe_allow_html=True)
