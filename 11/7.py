def find_even_numbers(n, m):
    even_numbers = [i for i in range(-n, n+1, m) if i % 2 == 0]
    return even_numbers

n = 20  # Значення n
m = 3   # Порядковий номер студента

result = find_even_numbers(n, m)
print("Парні числа від -{} до {} з кроком {}:".format(n, n, m))
print(result)