a = int(input())
b = int(input())
c = int(input())

MAX = max(a,b,c)
MIN = min(a,b,c)

if MIN == a and MAX == b:
    print(b)
    print(a)
    print(c)
elif MIN == b and MAX == c:
    print(c)
    print(b)
    print(a)
elif MIN == c and MAX == a:
    print(a)
    print(c)
    print(b)
elif MIN == a and MAX == c:
    print(c)
    print(a)
    print(b)
elif MIN == c and MAX == b:
    print(b)
    print(c)
    print(a)
elif MIN == b and MAX == a:
    print(a)
    print(b)
    print(c)