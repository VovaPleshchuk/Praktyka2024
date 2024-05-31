x = 10
y = 20
z = 30
str1 = "Hello"
str2 = "Para"
str3 = "UKD"

result1 = (x < y) or (str1 == str2)
result2 = (str1 != str2) or (str3 == "UKD")

result3 = (x > y) or (str1 == str2)
result4 = (str1 == "Hi") or (str2 == "UKD")

print("Результат 1 (істина):", result1)
print("Результат 2 (істина):", result2)
print("Результат 3 (хибність):", result3)
print("Результат 4 (хибність):", result4)
