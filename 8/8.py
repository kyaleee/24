with open('k7c-5.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
for i in range(len(a) - 4):
    if a[i] != a[i+1] and a[i+1] != a[i+2] and a[i+2] != a[i+3] and a[i+3] != a[i+4]:
        curl += 1
print(curl)
