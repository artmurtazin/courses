a = [int(x) for x in input().split()]
b = sorted(a)
d = ' '

for i in b:
    if b.count(i) > 1 and d != i:
        d = i
        print(i, end=' ')