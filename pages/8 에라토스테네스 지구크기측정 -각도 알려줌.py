import math

def calculate_theta(base, height):
    theta_radians = math.atan(height / base)  # 아크탄젠트 계산 (라디안 단위)
    theta_degrees = math.degrees(theta_radians)  # 라디안을 도(degree)로 변환
    return theta_degrees

# 사용자 입력 받기
try:
    base = float(input("밑변(막대기 길이)을 입력하세요: "))
    height = float(input("높이(그림자 길이)을 입력하세요: "))
    
    if base > 0 and height > 0:
        theta = calculate_theta(base, height)
        print(f"세타(θ) 값: {theta:.2f}°")
    else:
        print("오류: 밑변과 높이는 양수여야 합니다.")
except ValueError:
    print("오류: 숫자를 입력해야 합니다.")
