import random
import string

# Задаем количество дорог
num_roads = 10

# Генерируем уникальные идентификаторы для дорог
roads = [''.join(random.choices(string.ascii_uppercase, k=2)) for _ in range(num_roads)]
