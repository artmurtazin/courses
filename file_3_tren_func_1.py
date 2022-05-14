def min(*a):
    m = a[0]
    for x in a:
        if m > x:
            m = x
    return m

print(min(5))
print(min(5,3))
print(min(5,3,6,10))
print(min([5,3,6,10]))