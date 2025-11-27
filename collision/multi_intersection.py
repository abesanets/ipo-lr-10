from .rect_check import isCorrectRect, RectCorrectError
from .intersection_area import intersectionAreaRect

def intersectionAreaMultiRect(rectangles):
    """
    Вычисляет общую площадь пересечения всех переданных прямоугольников,
    учитывая только уникальные области пересечения без повторений.
    
    Args:
        rectangles: список прямоугольников [[(x1,y1),(x2,y2)], ...]
    
    Returns:
        float: общая уникальная площадь пересечения
    
    Raises:
        RectCorrectError: если какой-либо прямоугольник некорректен
    """
    if not rectangles:
        return 0.0
    
    # Проверяем корректность всех прямоугольников
    for i, rect in enumerate(rectangles):
        if not isCorrectRect(rect):
            raise RectCorrectError(f"Прямоугольник {i+1} некорректен")
    
    # Используем метод "разности площадей" для вычисления уникальной площади пересечения
    # Это более эффективный подход чем попиксельное сканирование
    
    # Если только один прямоугольник - возвращаем его площадь
    if len(rectangles) == 1:
        (x1, y1), (x2, y2) = rectangles[0]
        return (x2 - x1) * (y2 - y1)
    
    # Функция для вычисления площади прямоугольника
    def rect_area(rect):
        (x1, y1), (x2, y2) = rect
        return (x2 - x1) * (y2 - y1)
    
    # Функция для нахождения пересечения двух прямоугольников
    def intersect_two(rect1, rect2):
        (x1, y1), (x2, y2) = rect1
        (x3, y3), (x4, y4) = rect2
        
        x_left = max(x1, x3)
        x_right = min(x2, x4)
        y_bottom = max(y1, y3)
        y_top = min(y2, y4)
        
        if x_right > x_left and y_top > y_bottom:
            return [(x_left, y_bottom), (x_right, y_top)]
        return None
    
    # Используем принцип включения-исключения для вычисления общей площади пересечения
    # Это эффективный математический подход
    
    total_area = 0
    n = len(rectangles)
    
    # Генерируем все возможные комбинации прямоугольников (от 1 до n)
    from itertools import combinations
    
    # Применяем принцип включения-исключения
    for k in range(1, n + 1):
        sign = (-1) ** (k - 1)  # Чередование знаков
        
        # Для каждой комбинации из k прямоугольников
        for combo in combinations(rectangles, k):
            # Находим общее пересечение этих k прямоугольников
            current_intersection = combo[0]
            
            for rect in combo[1:]:
                current_intersection = intersect_two(current_intersection, rect)
                if current_intersection is None:
                    break
            
            if current_intersection is not None:
                area = rect_area(current_intersection)
                total_area += sign * area
    
    return total_area