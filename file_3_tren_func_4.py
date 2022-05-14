def modify_list(lst):
    global l
 #   l = lst
    f = []
    for i in l:
        if i % 2 == 0:
            f.append(int(i/2))

    l = f

l = [1, 2, 3, 4, 5, 6]
print(modify_list(l))  # None
print(l)               # [1, 2, 3]
modify_list(l)
print(l)               # [1]

l1 = [10, 5, 8, 3]
modify_list(l1)
print(l1)               # [5, 4]