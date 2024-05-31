a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

negative_count = 0

if a < 0:
    negative_count += 1
if b < 0:
    negative_count += 1
if c < 0:
    negative_count += 1

print(f"Кількість негативних чисел: {negative_count}")
