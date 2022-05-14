# #a = int(input())
# #a = [int(x) for x in input().split()]
# a = [2, 2, 3, -2, -2, -3, -4]

# for i in range(0, len(a)):
#     p = p + a[i]
#     if p == 0:
#         for j in range(0, i + 1):
#             s = s + a[j] * a[j]
# print(s)
i = 0
b = 0
a = []
p = 0
sum = 0

while True:
    b = int(input())
    a.append(b)
    sum = sum + a[i]
    p = p + a[i]*a[i]
    i += 1
    if sum == 0:
        print(p)
        break
