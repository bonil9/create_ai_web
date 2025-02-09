import math

def calculate_angle(base, height):
    """
    밑변(base)과 높이(height)를 이용하여 각도(theta)를 계산하는 함수
    """
    if base == 0:
        return "밑변이 0이면 각도를 계산할 수 없습니다."
    
    theta_rad = math.atan(height / base)  # 라디안 단위의 각도 계산
    theta_deg = math.degrees(theta_rad)  # 도 단위 변환
    
    return theta_deg

# 예제 실행
if __name__ == "__main__":
    base = float(input("막대기 길이를 입력하세요:(예시:12.2) cm 단위는 쓰지 마세요"))
    height = float(input("그림자 길이를 입력하세요:(예시:5.6) cm 단위는 쓰지 마세요"))
    angle = calculate_angle(base, height)
    print(f"계산된 각도: {angle:.2f}°")
