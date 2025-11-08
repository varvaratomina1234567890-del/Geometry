
def area(a, b): 
    '''Принимает число a b b возвращает произведение a и b'''
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return a * b


def perimeter(a, b):
    '''Принимает число a, возвращает произведение числа 2 на сумму a и b'''
    if a < 0 or b < 0:
        raise ValueError("Стороны не могут быть отрицательными")
    return 2 * (a+b)
