with open("k8-0.txt", "r") as F:
    s = F.readline()
maxLen, curLen, c = 1, 1, [s[0]]
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        curLen += 1
        if curLen == maxLen:
            c.append(s[i])
        elif curLen > maxLen:
            maxLen = curLen
            c = [s[i]]
    else:
        curLen = 1
for c1 in c:
    print(c1, maxLen)
