lst = [int(x) for x in input().split()]
x = int(input())

if x not in lst:
    print('Отсутствует')

for i in range(0, len(lst)):
    if lst[i] == x:
        print(i, end = ' ')

