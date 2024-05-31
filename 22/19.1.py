import math


def determine_century(year):
    century = math.ceil(year / 100)
    return century


print(determine_century(1900))
print(determine_century(1901))
print(determine_century(2000))
print(determine_century(2001))
print(determine_century(2024))
