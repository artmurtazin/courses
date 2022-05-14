a = int(input())
b = []

for i in range(1, a+1):
    b = b + [i]*i
    print(b[i-1], end = ' ')