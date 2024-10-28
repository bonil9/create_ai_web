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
    <style>
        html, body {{
            height: 1000px;
            margin: 0;
            display: flex;
            flex-direction: column;
        }}
        #top-frame {{
            flex: 8;
            overflow: auto;
        }}
        #bottom-frame {{
            flex: 2;
            overflow: hidden;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        #intro {{
            text-align: right;
            margin-bottom: 20px;
        }}
        img {{
            width: 600px;
        }}
    </style>
</head>
<body>
    <div id="top-frame">
        <div id="intro">너에 대해 소개 해봐</div>
        <div id="typed-output" style="margin-top: 20px;"></div>
    </div>
    <div id="bottom-frame">
        <img src="https://postfiles.pstatic.net/MjAyNDEwMjhfOTAg/MDAxNzMwMTE0ODc1ODgy.YmcUpDRZd2DFYHGODkvulWwiaRed14YbQ0jgBKFubCMg.pLvl3LZTCTYNExOkmZt_j9EYkDqU72Ob0YdpJhgzYbkg.PNG/SE-933f95e1-9960-4310-8302-7fdb4fbc1783.png?type=w773" alt="Intro Image">
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // '너에 대해 소개 해봐' 글을 먼저 표시하고, 그 다음 타이핑 효과 시작
            setTimeout(function() {{
                var typed = new Typed("#typed-output", {{
                    strings: [{typed_text!r}],
                    typeSpeed: 120,
                    backSpeed: 50,
                    showCursor: true,
                    cursorChar: "|",
                    loop: false
                }});
            }}, 1000); // 1초 후 타이핑 효과 시작
        }});
    </script>
</body>
</html>
""")
