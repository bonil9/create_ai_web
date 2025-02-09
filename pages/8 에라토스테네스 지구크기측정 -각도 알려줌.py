import math
import streamlit as st

def calculate_angle(base, height):
    if base == 0:
        return "밑변이 0이면 각도를 계산할 수 없습니다."
    
    theta_rad = math.atan(height / base)
    theta_deg = math.degrees(theta_rad)
    
    return theta_deg

st.title("에라토스테네스의 지구크기 측정 각도 계산")


base = st.number_input("막대기 길이를 입력하세요:(예시:12.2)(단위는 쓰지마세요)", min_value=0.0, format="%.2f")
height = st.number_input("그림자 길이를 입력하세요:(예시:3.2)(단위는 쓰지마세요)", min_value=0.0, format="%.2f")

if st.button("계산하기"):
    angle = calculate_angle(base, height)
    st.write(f"계산된 각도: {angle:.2f}°")
