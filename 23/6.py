a = int(input("Введіть перше число (a): "))
b = int(input("Введіть друге число (b): "))

if a == b:
    a = 0
    b = 0
else:
    max_value = max(a, b)
    a = max_value
    b = max_value

print(f"Нове значення a: {a}")
print(f"Нове значення b: {b}")
