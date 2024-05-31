def special_message(value):
    if value > 0:
        print("Значення змінної більше за 0!")
        return 1
    elif value < 0:
        print("Значення змінної менше за 0!")
        return -1
    else:
        print("Значення змінної рівне 0.")
        return None

variable = 5
result = special_message(variable)
print("Результат:", result)

variable = -3
result = special_message(variable)
print("Результат:", result)
