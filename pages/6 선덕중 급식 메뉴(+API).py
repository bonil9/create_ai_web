import requests
import json
import pandas as pd
import streamlit as st

# 출력 상단 제목 추가
st.title('도촌초등학교 급식 메뉴 알아보기')

# NEIS API 기본 정보 설정
api_key = 'e0ebc693609640248fc0cdb50b3e5b82'
base_url = 'https://open.neis.go.kr/hub/mealServiceDietInfo'

# Streamlit을 사용하여 날짜 입력 받기
input_date = st.date_input('날짜를 선택하세요:').strftime('%Y%m%d')

if input_date:
    # 요청 파라미터 설정
    params = {
        'ATPT_OFCDC_SC_CODE': 'K10',        # 시도 교육청 코드
        'SD_SCHUL_CODE': '7952013',          # 학교 코드
        'MLSV_YMD': input_date,              # 입력 받은 날짜 (YYYYMMDD 형식)
        'KEY': api_key,                      # API 키
        'Type': 'json'                       # 응답 형식
    }

    # API 요청 보내기
    response = requests.get(base_url, params=params)

    # 응답 처리
    if response.status_code == 200:
        data = response.json()
        if 'mealServiceDietInfo' in data and 'row' in data['mealServiceDietInfo'][1]:
            meal_info = data['mealServiceDietInfo'][1]['row']
            if meal_info:
                # 데이터를 DataFrame으로 변환
                meal_data = []
                for meal in meal_info:
                    meal_data.append({
                       '메뉴': meal['DDISH_NM'].replace('<br/>', ', ')
                    })
                df = pd.DataFrame(meal_data)
                # Streamlit을 사용해 DataFrame을 표시
                st.dataframe(df, use_container_width=True)
            else:
                st.write("해당 날짜의 급식 정보가 없습니다.")
        else:
            st.write("급식 정보가 올바르게 수신되지 않았습니다. 데이터 구조를 확인하세요.")
    else:
        st.write(f"API 요청 실패: {response.status_code}")
