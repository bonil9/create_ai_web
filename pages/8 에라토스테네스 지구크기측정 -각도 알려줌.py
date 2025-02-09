import math
import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_theta(base, height):
    theta_radians = math.atan(height / base)  # 아크탄젠트 계산 (라디안 단위)
    theta_degrees = math.degrees(theta_radians)  # 라디안을 도(degree)로 변환
    return theta_degrees

def get_input():
    root = tk.Tk()
    root.withdraw()  # 기본 창 숨기기
    
    base = simpledialog.askfloat("입력", "밑변(막대기 길이)을 입력하세요:")
    height = simpledialog.askfloat("입력", "높이(그림자 길이)을 입력하세요:")
    
    if base and height:
        theta = calculate_theta(base, height)
        messagebox.showinfo("결과", f"세타(θ) 값: {theta:.2f}°")
    else:
        messagebox.showerror("오류", "올바른 값을 입력하세요.")

# 실행
get_input()
