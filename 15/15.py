with open('k8-1.txt', 'r') as f:
    a = f.readline()
b = 0
c = 0
m = 0
for i in range(1, len(a)):
    if a[i] != a[i-1]:
        b += 1
        if b > m:
            m = b
    else:
        b = 1
print(m)