import os
import streamlit as st
import google.generativeai as genai

# 사이드바에서 API 키 입력 받기
st.sidebar.title("API 설정")
api_key = st.sidebar.text_input("Google Gemini API 키를 입력하세요", type="password")

# API 키가 입력되었는지 확인
if api_key:
    # API 키 설정
    os.environ['API_KEY'] = api_key
    genai.configure(api_key=os.environ['API_KEY'])

    # Streamlit 페이지 제목 설정
    st.title("인공지능 그림 생성기")

    # 사용자가 생성하고자 하는 그림에 대한 설명 입력
    user_prompt = st.text_area("생성할 그림에 대한 설명을 입력하세요")

    number_of_images = st.slider("생성할 이미지 수", 1, 4, 1)
    aspect_ratio = st.selectbox("이미지 비율 선택", ["1:1", "3:4", "4:3", "16:9"], index=1)

    if st.button("그림 생성"):
        if user_prompt:
            try:
                # 이미지 생성 요청
                result = genai.generate_images(
                    prompt=user_prompt,
                    num_images=number_of_images,
                    aspect_ratio=aspect_ratio
                )

                # 응답이 이미지 데이터일 경우 출력
                if result and hasattr(result, 'images') and result.images:
                    for i, image in enumerate(result.images):
                        st.image(image._pil_image, caption=f"생성된 그림 {i+1}")
                else:
                    st.warning("이미지를 생성할 수 없습니다. 다른 설명을 시도해보세요.")
            except Exception as e:
                st.error(f"그림 생성 중 오류가 발생했습니다: {e}")
        else:
            st.warning("생성할 그림에 대한 설명을 입력하세요.")
else:
    st.warning("API 키를 사이드바에 입력하세요.")
