# -*- coding: utf-8 -*-
"""計算圓周長和面積

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Qc5N8aV-IAEU9OM6Ckt59ZcvGS3eIudO
"""

import math

def calculate_circle(radius):
    # 計算圓的周長
    circumference = 2 * math.pi * radius
    # 計算圓的面積
    area = math.pi * radius ** 2
    return circumference, area

if __name__ == "__main__":
    try:
        # 使用者輸入半徑
        radius = float(input("請輸入圓的半徑："))

        # 呼叫函數計算圓的周長和面積
        circumference, area = calculate_circle(radius)

        # 輸出結果
        print("圓的周長為：", circumference)
        print("圓的面積為：", area)

    except ValueError:
        print("請輸入一個有效的數字作為半徑。")