with open('24.txt', 'r') as f:
    a = f.readline()
asc = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
curl = 0
maxl = 0

for i in range(1, len(a)):
    if a[i] != '\n':
        if asc.index(a[i]) > asc.index(a[i-1]):
            curl += 1
            if curl > maxl:
                maxl = curl
        else:
            curl = 1
print(maxl)