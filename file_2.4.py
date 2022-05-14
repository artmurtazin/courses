s = input()
i = 1
cnt = 1
p = ''
k = len(s)

if k == 1:
    print(s[0] + str(k))


for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
            i += 1
            if i == len(s):
                p = p + s[i-1] + str(cnt)
        else:
            p = p + s[i-1] + str(cnt)
            cnt = 1
            i += 1
            if i == len(s):
                p = p + s[i-1] + str(cnt)
print(p)