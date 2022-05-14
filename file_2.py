a = 0

while True:
    a = int(input())
    if a <= 100 and a >= 10:
        print (a)
    if a > 100:
        break
    if a < 10:
        continue