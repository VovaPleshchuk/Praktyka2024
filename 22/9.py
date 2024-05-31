def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib

fib_sequence = fibonacci(20)
print("Ряд чисел Фібоначчі від п'ятого до двадцятого члена:")
for num in fib_sequence[4:20]:
    print(num, end=" ")

print("\nРяд парних чисел від 0 до 20:")
for i in range(0, 21, 2):
    print(i, end=" ")

print("\nКожне третє число від -1 до -21:")
for i in range(-1, -22, -3):
    print(i, end=" ")

print("\nРяд чисел Фібоначчі до 20-го члена:")
for num in fib_sequence:
    print(num, end=" ")

