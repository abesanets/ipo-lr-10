from .rect_check import isCorrectRect, RectCorrectError
from .collision_detection import isCollisionRect
from .intersection_area import intersectionAreaRect
from .multi_intersection import intersectionAreaMultiRect

__all__ = [
    'isCorrectRect', 
    'isCollisionRect', 
    'intersectionAreaRect', 
    'intersectionAreaMultiRect', 
    'RectCorrectError'
]