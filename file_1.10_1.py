a = int(input())
b = int(input())
h = int(input())

if h > a and h < b:
    print('Это нормально')

if h <= a:
    print('Недосып')

if h >= b:
    print('Пересып')