    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const inputElement = window.parent.document.querySelector('input[type="text"]');
            if (inputElement) {
                inputElement.focus();
                inputElement.setSelectionRange(inputElement.value.length, inputElement.value.length);  // 커서를 '메시지 RecordAI' 뒤에 위치시킴
                inputElement.style.caretColor = "black";  // 커서 색상을 명확하게 표시
                setInterval(function() {{
                    if (inputElement.style.caretColor === "transparent") {{
                        inputElement.style.caretColor = "black";
                    }} else {{
                        inputElement.style.caretColor = "transparent";
                    }}
                }}, 500);  // 깜박이는 효과 추가
            }
        });
    </script>
    """, height=0)

focus_input()
user_input = st.text_input("", "메시지 RecordAI")

# 입력된 텍스트 출력 (필요한 경우 다른 용도로 사용할 수 있음)
st.write(f"")