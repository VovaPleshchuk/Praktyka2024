x = 10
y = 20
z = 30
str1 = "Hello"
str2 = "UKD"
str3 = "Para"

result1 = (x < y) or (str1 == str2)  # True or False = True
result2 = (str1 != str2) or (str3 == "Python")  # True or True = True

result3 = (x > y) or (str1 == str2)  # False or False = False
result4 = (str1 == "Hi") or (str2 == "Python")  # False or False = False

print("Результат 1 (істина):", result1)
print("Результат 2 (істина):", result2)
print("Результат 3 (хибність):", result3)
print("Результат 4 (хибність):", result4)
