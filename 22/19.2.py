import random

random_numbers = [random.randint(1, 10) for _ in range(10)]

print("Згенеровані числа:", random_numbers)

average = sum(random_numbers) / len(random_numbers)

print("Середнє арифметичне:", average)
