x = float(input("Введіть перше число (x): "))
y = float(input("Введіть друге число (y): "))

if x == y:
    print("Числа не повинні бути рівні одне одному.")
else:

    half_sum = (x + y) / 2
    double_product = 2 * x * y

    if x < y:
        x_new = half_sum
        y_new = double_product
    else:
        x_new = double_product
        y_new = half_sum

    print(f"Нове значення x: {x_new}")
    print(f"Нове значення y: {y_new}")
