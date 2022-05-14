#for i in range(0, 3):
b = []
p = []
y = []
a = []
w = []
o = []
l = []

while True:
    if p != ['end']:
        p = [str(x) for x in input().split()]
        if p == ['end']:
            break
        y = p
        b = b + [p]

n = len(y)      # количество столбцов
m = len(b)      # количество строк

#
#      for j in range(n):
#         w = list(map(int, b[i][j]))
for i in range(m):
    w = list(map(int, b[i]))
    o = w
    l = l +[w]

# for i, item in enumerate(y):
#     a[i] = int(item)

# for i in range(m*n):
#     for j in range(m*n):
#         b[i][j] = int(b[i][j])

#print('m =', m)
#print('n =', n)
# print('y =', y)
# print('l =', l)
# print('w =', w)
# print('b[1][1] =', b[1][1])
# q = [-5, 2, 9]
# print('q =', q)

s = [[0]*n for h in range(m)]

if m + n == 2:
    print(l[0][0]+l[0][0]+l[0][0]+l[0][0])

if (m == n) and n != 1:
    for i in range(-1, m-1):
        for j in range(-1, n-1):
            s[i][j] = l[i-1][j] + l[i+1][j] + l[i][j-1] + l[i][j+1]

    for i in range(0, n):
        for j in range(0, m):
            if j == m-1:
                print(s[i][j], end='\n')
            else:
                print(s[i][j], end=' ')

if m > n and (m > 1 and n > 1):
    for i in range(-m, 0):
        for j in range(-n, 0):
            #s[i][j] = l[i+3][j] + l[i+1][j] + l[i][j+3] + l[i][j+1]
            s[i][j] = l[i + 1][j] + l[i + (m-1)][j] + l[i][j + 1] + l[i][j + (n-1)]

    for i in range(-m, 0):
        for j in range(-n, 0):
            if j == -1:
                print(s[i][j], end='\n')
            else:
                print(s[i][j], end=' ')


if m < n and (m > 1 and n > 1):
    for i in range(-1, m-1):
        for j in range(-1, n-1):
            s[i][j] = l[i-1][j] + l[i+1][j] + l[i][j-1] + l[i][j+1]

    for i in range(-m, 0):
        for j in range(-n, 0):
            if j == -1:
                print(s[i][j], end='\n')
            else:
                print(s[i][j], end=' ')

if m == 1 and n > 1:
    for j in range(-n, 0):
        s[0][j] = l[0][j] + l[0][j] + l[0][j + (n-1)] + l[0][j + 1]

    for j in range(-n, 0):
        print(s[0][j], end=' ')

if n == 1 and m > 1:
    for i in range(-m, 0):
        #s[i][0] = l[i][0] + l[i][0] + l[i + 2][0] + l[i + 1][0]
        s[i][0] = l[i][0] + l[i][0] + l[i + (m-1)][0] + l[i + 1][0]

    for i in range(-m, 0):
        print(s[i][0], end='\n')