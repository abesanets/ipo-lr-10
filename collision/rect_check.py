def isCorrectRect(points):
    """
    Проверяет корректность введенных координат прямоугольника.
    
    Args:
        points: список из двух кортежей [(x1, y1), (x2, y2)]
                где (x1, y1) - левый нижний угол
                (x2, y2) - правый верхний угол
    
    Returns:
        bool: True если координаты корректны, False в противном случае
    """
    if len(points) != 2:
        return False
    
    left_bottom, right_top = points
    
    # Проверяем что оба элемента являются кортежами
    if not (isinstance(left_bottom, tuple) and isinstance(right_top, tuple)):
        return False
    
    # Проверяем что в каждом кортеже по 2 элемента
    if not (len(left_bottom) == 2 and len(right_top) == 2):
        return False
    
    # Проверяем что все элементы являются числами
    if not all(isinstance(coord, (int, float)) for coord in left_bottom + right_top):
        return False
    
    x1, y1 = left_bottom
    x2, y2 = right_top
    
    # Проверяем что левый нижний угол действительно левее и ниже правого верхнего
    if x1 >= x2 or y1 >= y2:
        return False
    
    return True

