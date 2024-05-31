x = 10
y = 20
z = 30

result1 = (x < y) and (y < z)
result2 = (x != z) and (y > x)

result3 = (x > y) and (y < z)
result4 = (x == z) and (y < x)

print("Результат 1 (істина):", result1)
print("Результат 2 (істина):", result2)
print("Результат 3 (хибність):", result3)
print("Результат 4 (хибність):", result4)
