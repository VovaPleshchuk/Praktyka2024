num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

def process_number(num):
    if num >= 0:
        return num ** 2
    else:
        return num ** 4

result1 = process_number(num1)
result2 = process_number(num2)
result3 = process_number(num3)

print(f"Оброблене перше число: {result1}")
print(f"Оброблене друге число: {result2}")
print(f"Оброблене третє число: {result3}")
