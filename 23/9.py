a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

integer_count = 0

if a.is_integer():
    integer_count += 1
if b.is_integer():
    integer_count += 1
if c.is_integer():
    integer_count += 1

print(f"Кількість цілих чисел: {integer_count}")
