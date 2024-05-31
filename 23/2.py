import math

x1 = float(input("Введіть координату x1 для точки A: "))
y1 = float(input("Введіть координату y1 для точки A: "))
x2 = float(input("Введіть координату x2 для точки B: "))
y2 = float(input("Введіть координату y2 для точки B: "))

def distance_from_origin(x, y):
    return math.sqrt(x**2 + y**2)

distance_A = distance_from_origin(x1, y1)
distance_B = distance_from_origin(x2, y2)

if distance_A < distance_B:
    print("Точка A ближче до початку координат.")
elif distance_A > distance_B:
    print("Точка B ближче до початку координат.")
else:
    print("Обидві точки знаходяться на однаковій відстані від початку координат.")
