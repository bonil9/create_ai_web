import requests
import xml.etree.ElementTree as ET
from datetime import datetime
import streamlit as st

def get_seodaemun_education_services(api_key, selected_date, start_index=1, end_index=100):
    # API 요청 URL 생성
    url = f"http://openapi.seoul.go.kr:8088/{api_key}/xml/ListPublicReservationEducation/{start_index}/{end_index}/"
    
    # API 요청
    response = requests.get(url)
    
    # 요청 성공 여부 확인
    if response.status_code == 200:
        # XML 파싱
        root = ET.fromstring(response.content)
        
        # 서비스 정보 출력 여부 확인 변수
        found_services = False
        
        # 서비스 정보 출력
        for row in root.iter("row"):
            service_name = row.find("SVCNM").text if row.find("SVCNM") is not None else "N/A"
            service_location = row.find("PLACENM").text if row.find("PLACENM") is not None else "N/A"
            start_date = row.find("SVCOPNBGNDT").text if row.find("SVCOPNBGNDT") is not None else None
            end_date = row.find("SVCOPNENDDT").text if row.find("SVCOPNENDDT") is not None else None
            
            # 날짜 필터 적용
            if start_date and end_date:
                try:
                    # 날짜 형식 파싱 수정
                    if "-" in start_date or " " in start_date:
                        start_date_obj = datetime.strptime(start_date.split()[0], "%Y-%m-%d")
                    else:
                        start_date_obj = datetime.strptime(start_date, "%Y%m%d")
                    
                    if "-" in end_date or " " in end_date:
                        end_date_obj = datetime.strptime(end_date.split()[0], "%Y-%m-%d")
                    else:
                        end_date_obj = datetime.strptime(end_date, "%Y%m%d")
                    
                    selected_date_obj = datetime.strptime(selected_date, "%Y-%m-%d")
                    
                    # 서비스가 선택된 날짜 범위 내에 있는 경우만 출력
                    if start_date_obj <= selected_date_obj <= end_date_obj:
                        st.write(f"**서비스 이름**: {service_name}")
                        st.write(f"**위치**: {service_location}")
                        st.write(f"**시작 날짜**: {start_date_obj.strftime('%Y-%m-%d')}")
                        st.write(f"**종료 날짜**: {end_date_obj.strftime('%Y-%m-%d')}")
                        st.write("-" * 30)
                        found_services = True
                except ValueError as e:
                    st.write(f"날짜 파싱 오류 서비스: {service_name}, 오류: {e}")
        
        # 검색된 서비스가 없을 경우 메시지 출력
        if not found_services:
            st.write("선택한 날짜에 이용 가능한 서비스가 없습니다.")
    else:
        st.write(f"데이터를 가져오는 데 실패했습니다: {response.status_code}")

# Streamlit UI
def main():
    st.title("서울시 교육정보 확인하기")
    api_key = "767063424f7361793131334167597278"
    
    # 날짜 입력받기 (오늘 날짜로 초기값 설정)
    selected_date = st.date_input("날짜 선택 (YYYY-MM-DD)", value=datetime.today(), format="YYYY-MM-DD")
    
    if st.button("서비스 검색"):
        get_seodaemun_education_services(api_key, selected_date.strftime("%Y-%m-%d"))

if __name__ == "__main__":
    main()
