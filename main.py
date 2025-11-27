from collision import isCorrectRect

# Примеры из задания
print(isCorrectRect([(-3.4, 1), (9.2, 10)]))  # Вернет True
print(isCorrectRect([(-7, 9), (3, 6)]))       # Вернет False

# Дополнительные тесты
print(isCorrectRect([(0, 0), (5, 5)]))        # True
print(isCorrectRect([(5, 0), (0, 5)]))        # False (x1 > x2)
print(isCorrectRect([(0, 5), (5, 0)]))        # False (y1 > y2)
print(isCorrectRect([(0, 0), (0, 5)]))        # False (x1 == x2)