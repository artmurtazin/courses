figure = input()
if figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c)/2
    S = (p * (p - a)*(p - b)*(p - c))**0.5
    print(S)

if figure == 'прямоугольник':
    a = int(input())
    b = int(input())
    S = a * b
    print(S)

if figure == 'круг':
    r = int(input())
    S = 3.14 * r**2
    print(S)