from .rect_check import isCorrectRect
from .collision_detection import isCollisionRect

def intersectionAreaRect(rect1, rect2):
    """
    Вычисляет площадь пересечения двух прямоугольников.
    
    Args:
        rect1: первый прямоугольник [(x1, y1), (x2, y2)]
        rect2: второй прямоугольник [(x3, y3), (x4, y4)]
    
    Returns:
        float: площадь пересечения прямоугольников, 0 если не пересекаются
    
    Raises:
        ValueError: если один из прямоугольников некорректен
    """
    # Проверяем корректность первого прямоугольника
    if not isCorrectRect(rect1):
        raise ValueError("Первый прямоугольник некорректен")
    
    # Проверяем корректность второго прямоугольника
    if not isCorrectRect(rect2):
        raise ValueError("Второй прямоугольник некорректен")
    
    # Если прямоугольники не пересекаются, возвращаем 0
    if not isCollisionRect(rect1, rect2):
        return 0.0
    
    # Извлекаем координаты первого прямоугольника
    (x1, y1), (x2, y2) = rect1
    
    # Извлекаем координаты второго прямоугольника
    (x3, y3), (x4, y4) = rect2
    
    # Находим координаты пересечения по оси X
    x_left = max(x1, x3)    # Левый край пересечения
    x_right = min(x2, x4)   # Правый край пересечения
    
    # Находим координаты пересечения по оси Y
    y_bottom = max(y1, y3)  # Нижний край пересечения
    y_top = min(y2, y4)     # Верхний край пересечения
    
    # Вычисляем ширину и высоту области пересечения
    width = x_right - x_left
    height = y_top - y_bottom
    
    # Вычисляем площадь пересечения
    area = width * height
    
    return area