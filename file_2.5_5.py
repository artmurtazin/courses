a = [int(x) for x in input().split()]
sum = 0

if len(a) == 1:
    sum = a[0]
    print(str(sum))
else:
    for i in range(0, len(a)):
        if i == len(a) - 1:
            sum = a[i - 1] + a[0]
            print(str(sum))
        else:
            sum = a[i - 1] + a[i + 1]
            print(str(sum), end=' ')



