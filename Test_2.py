#p = [int(x) for x in input().split()]

#for i in range(0, 3):
b = []
p = 0
q = 0
q2 = 0

for i in range(0, 10):
    q = input()
    if q == 'end':
        break
    if q != 'end':
        #p = [int(x) for x in input().split()]
        p = list(q)
        print(p)
        #p.append(q)
        y = p
        b = b + [p]

print(b)