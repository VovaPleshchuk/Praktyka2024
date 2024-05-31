import math

def calculate_circle_area(radius):
    return math.pi * (radius ** 2)

radius = float(input("Введіть радіус кола: "))

area = calculate_circle_area(radius)

print(f"Площа кола з радіусом {radius} дорівнює {area:.2f}")
