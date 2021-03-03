with open('24-1.txt', 'r') as f:
    a = f.readline()
maxl = 99999999999999
num = []
cur = ''
for i in range(1, len(a) - 1):
    if a[i].isdigit():
        cur += a[i]
        if i == len(a) - 1:
            num.append(int(cur))
    else:
        if cur != '':
            num.append(int(cur))
            cur = ''
for i in num:
    if i % 2 != 0 and i < maxl:
        maxl = i
print(maxl)
