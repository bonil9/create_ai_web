import streamlit as st
import google.generativeai as genai

# API 키 설정
api_key = ""

# API 키 설정
if api_key:
    genai.configure(api_key=api_key)

    # Streamlit 페이지 제목 설정
    st.title("인공지능 상장 생성기")

    # 생성 설정
    generation_config = {
        "temperature": 1,
        "top_p": 0.95,
        "top_k": 64,
        "max_output_tokens": 8192,
        "response_mime_type": "text/plain",
    }

    # 모델 초기화
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        generation_config=generation_config,
    )

    # 사용자 입력 받기
    user_input = st.text_area("상장을 생성할 내용을 입력하세요", 
                              "예: 민수는 체육대회에서 친구들과 함께 열심히 뛰면서 서로 응원하고 도와주었어요.")

    if st.button("상장 생성"):
        # 인공지능 모델을 사용하여 상장 생성
        response = model.generate_content([
            "초등학생에게 평소 생활을 반영하는 상장을 수여하고자 합니다. 입력의 내용을 참고하여 재치있는 상장명과 문구를 생성해주세요.",
            f"input: {user_input}",
        ])

        # 결과 출력
        st.subheader("생성된 상장")
        st.write(response.text)
