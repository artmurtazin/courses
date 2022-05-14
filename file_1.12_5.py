a = int(input())
b = int(input())
c = int(input())

while True:
    if a >= c and a >= b:
        print(a)
        break
    if b >= c and b >= a:
        print(b)
        break
    if c >= b and c >= a:
        print(c)
        break

while True:
    if a <= c and a <= b:
        print(a)
        break
    if b <= c and b <= a:
        print(b)
        break
    if c <= b and c <= a:
        print(c)
        break


while True:
    if a >= c and a <= b or a >= b and a <= c:
        print(a)
        break
    if b >= c and b <= a or b >= a and b <= c:
        print(b)
        break
    if c >= b and c <= a or c >= a and c <= b:
        print(c)
        break