def special_message(value):
    if value > 0:
        print("Значення змінної більше за 0!")
    elif value < 0:
        print("Значення змінної менше за 0!")
    else:
        print("Значення змінної рівне 0.")

variable = 7
special_message(variable)

variable = -3
special_message(variable)
