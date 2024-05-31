a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
c = float(input("Введіть третє число (c): "))

k = float(input("Введіть число k: "))

divisors = []

if a % k == 0:
    divisors.append(a)
if b % k == 0:
    divisors.append(b)
if c % k == 0:
    divisors.append(c)

if divisors:
    print(f"Числа {divisors} діляться на {k}.")
else:
    print(f"Жодне з введених чисел не ділиться на {k}.")
