# lst = [1, 1, 3, 2, 4, 5, 6, 8, -1, 7, 8, 9, -16, 0, 4]
# print(lst)
#
# def modify_list(l):
#     global lst
#     f = []
#     for i in l:
#         if i % 2 == 0:
#             f.append(int(i/2))
#     lst = f
#
#
# # lst = [1, 2, 3, 4, 5, 6]
# # print(modify_list(lst))  # None
# # print(lst)               # [1, 2, 3]
# # modify_list(lst)
# # print(lst)               # [1]
# #
# # lst = [10, 5, 8, 3]
# # modify_list(lst)
# # print(lst)
#
# print(modify_list(lst))
# print(lst)


n=input()

c=['1']
c1=['2','3','4']
c2=['0','5','6','7','8','9']
q=['2','3','4','5','6','7','8','9']
# print (len(n))
# print (n[0])

if int(n)>=10 and int(n)<=20:
    print (n, ' программистов')

#elif n>=100 and n<1000 and n[len(n)-2]==1:
#print (n, ' программистов')

else:
    if (n[len(n)-1] in c and len(n)==1) or (n[len(n)-1] in c and n[len(n)-2] in q):
        print (n, 'программист')

    elif n[len(n)-1] in c1 and n[len(n)-2] not in c:
        print (n, 'программиста')

    elif n[len(n)-1] in c2 or n[len(n)-2] in c:
        print (n, 'программистов')