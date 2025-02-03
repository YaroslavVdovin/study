import math

a = float(input('Введите длину 1-й стороны: '))
b = float(input('Введите длину 2-й стороны: '))
c = float(input('Введите длину 3-й стороны: '))

def area(a, b, c):
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    return S

print(area(a, b, c))