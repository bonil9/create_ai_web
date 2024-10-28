import streamlit as st
import streamlit.components.v1 as components

# 첫 화면 문구 추가 (타자치는 형태로 작성되는 효과 추가)
typed_text = """
RecordAI: 저는 물리를 좋아하는 과학교사 입니다. 특히 양자역학을, 귀납적사고와 연역적 사고 중심 수업을 지향합니다. 요즘 에듀테크 중 MBL 가능한 것과 ChatGPT에 관심을 가지고 있습니다. 개인적으로 많은 것을 기록하고자 합니다.
"""

# HTML과 JavaScript를 사용하여 타이핑 효과 추가
components.html(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://cdn.jsdelivr.net/npm/typed.js@2.0.12"></script>
</head>
<body>
    <div id="typed-output"></div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            var typed = new Typed("#typed-output", {{
                strings: [{typed_text!r}],
                typeSpeed: 50,
                backSpeed: 25,
                showCursor: true,
                cursorChar: "|",
                loop: false
            }});
        }});
    </script>
</body>
</html>
""")
