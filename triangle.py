def area(base, height):
    """Вычисляет площадь треугольника"""
    if base < 0 or height < 0:
        raise ValueError("Основание и высота не могут быть отрицательными")
    return 0.5 * base * height

def perimeter(a, b, c):
    """Вычисляет периметр треугольника"""
    if a < 0 or b < 0 or c < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    
    # Проверка неравенства треугольника
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError("Нарушено неравенство треугольника")
    
    return a + b + c