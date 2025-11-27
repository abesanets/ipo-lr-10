#-----------------ЗАДАНИЕ 2------------------
print("-----------------ЗАДАНИЕ 2------------------")

from collision import isCorrectRect

# Примеры из задания
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # Вернет True
print(isCorrectRect([(-7, 9), (3, 6)]))       # Вернет False
print()


#-----------------ЗАДАНИЕ 3------------------
print("-----------------ЗАДАНИЕ 3------------------")

from collision import isCollisionRect, RectCorrectError

# Примеры из задания
print(isCollisionRect([(-3.4, 1), (9.2, 10)], [(-7.4, 0), (13.2, 12)]))  # True
print(isCollisionRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))              # False

# Проверка ошибки
try:
    isCollisionRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])  # Вызовет ошибку
except RectCorrectError as e:
    print(f"Ошибка: {e}")
print()


#-----------------ЗАДАНИЕ 4------------------
print("-----------------ЗАДАНИЕ 4------------------")
from collision import intersectionAreaRect

# Примеры из задания
print(intersectionAreaRect([(-3, 1), (9, 10)], [(-7, 0), (13, 12)]))  # Положительное число
print(intersectionAreaRect([(1, 1), (2, 2)], [(3, 0), (13, 1)]))      # 0.0

# Проверка ошибки
try:
    intersectionAreaRect([(1, 1), (2, 2)], [(3, 17), (13, 1)])  # Вызовет ошибку
except ValueError as e:
    print(f"Ошибка: {e}")
print()


#-----------------ЗАДАНИЕ 5------------------
print("-----------------ЗАДАНИЕ 5------------------")
from collision import intersectionAreaMultiRect, RectCorrectError

# Пример из задания
rectangles = [
    [(-3, 1), (9, 10)],
    [(-7, 0), (13, 12)],
    [(0, 0), (5, 5)],
    [(2, 2), (7, 7)]
]
result = intersectionAreaMultiRect(rectangles)
print(f"Уникальная площадь пересечения: {result}")

# Проверка ошибки
try:
    incorrect_rectangles = [
        [(-3, 1), (9, 10)],
        [(3, 17), (13, 1)]  # Некорректный прямоугольник
    ]
    intersectionAreaMultiRect(incorrect_rectangles)
except RectCorrectError as e:
    print(f"Ошибка: {e}")
print()