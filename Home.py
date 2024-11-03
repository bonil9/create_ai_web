import streamlit as st
import streamlit.components.v1 as components

# 첫 화면 문구 추가 (타자치는 형태로 작성되는 효과 추가)
typed_text = """
RecordAI: 저는 물리를 좋아하는 과학교사 입니다. 특히 양자역학을,,,,, 과학 수업은 귀납적사고와 연역적 사고 중심 수업 지향해야 한다고 생각합니다. 그리고 요즘 에듀테크 중 MBL 가능한 것과 ChatGPT에 관심을 가지고 있습니다.  개인적으로 많은 것을 기록하고자 합니다.
"""

# HTML과 JavaScript를 사용하여 타이핑 효과 추가
components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
    <style>
        html, body {{
            height: 100%;
            margin: 0;
            display: flex;
            flex-direction: column;
        }}
        #top-frame {{
            flex: 8;
            overflow: auto;
        }}
        #bottom-frame {{
            flex: 1.5;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        #intro {{
            text-align: right;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div id="top-frame">
        <div id="intro">너에 대해 소개 해봐</div>
        <div id="typed-output" style="margin-top: 20px;"></div>
    </div>
    <div id="bottom-frame">
        <div id="streamlit-input">
            <p></p>
        </div>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // '너에 대해 소개 해봐' 글을 먼저 표시하고, 그 다음 타이핑 효과 시작
            setTimeout(function() {{
                var typed = new Typed("#typed-output", {{
                    strings: [{typed_text!r}],
                    typeSpeed: 6,  // 타이핑 속도 매우 빠르게 증가
                    backSpeed: 3,   // 백스페이스 속도 매우 빠르게 증가
                    showCursor: false,
                    loop: false
                }});
            }}, 1000); // 1초 후 타이핑 효과 시작
        }});
    </script>
</body>
</html>
""", height=400)

# Streamlit 입력창 추가
def focus_input():
    components.html("""
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
