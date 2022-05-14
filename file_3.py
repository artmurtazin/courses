while True:
    a = int(input())
    if a > 10:
        print('Введенно Вами число не должно быть больше 10')
        continue
    break

print('a =', a)

while True:
    b = int(input())
    if b > 10:
        print('Введенно Вами число не должно быть больше 10')
        continue
    if b < a:
        print('Введенно Вами число не должно быть меньше', a)
        continue
    break

print('b =', b)

while True:
    c = int(input())
    if c > 10:
        print('Введенно Вами число не должно быть больше 10')
        continue
    break

print('c =', c)

while True:
    d = int(input())
    if d > 10:
        print('Введенно Вами число не должно быть больше 10')
        continue
    if d < c:
        print('Введенно Вами число не должно быть меньше', c)
        continue
    break

print('d =', d)

for n in range(c, d + 1):
    print('\t', n, end='')

for i in range(a, b + 1):
    q = i
    print('')
    for j in range(c, d + 1):
        p = i*j
        if q == i:
            print(i, '\t', p, end='\t')
        else:
            print(p, end='\t')
        q += 1