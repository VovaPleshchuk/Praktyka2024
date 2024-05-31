import math

def count_combinations(m):
    if m > 25:
        return "Помилка: кількість комірок не може перевищувати 25"
    elif m <= 0:
        return "Помилка: кількість комірок повинна бути більше 0"
    else:
        return math.factorial(25) / math.factorial(25 - m)

m = int(input("Введіть кількість комірок (m): "))

print("Кількість можливих комбінацій:", count_combinations(m))