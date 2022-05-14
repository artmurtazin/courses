# n = int(input())
# max = n**2
# print(max)
# s = [[0]*n for h in range(n)]
# len = len(s)
# q = 1
# i_min = 1
# j_min = 1
#
# i_max = len
# j_max = len
#
# for i in range(-i_max, -i_max+1):
#     for j in range(-j_max, -j_min+1):
#         s[i][j] = q
#         q += 1
#         i_max += 1
#         j_max += 1
#         j_min += 1
#
# print(s)
# print('len = ',len)
#


numbers = [1, 2, 3, 4, 5]

for counter, item  in enumerate(numbers):
    if(counter % 2 == 0):
        print(item)

print(counter)