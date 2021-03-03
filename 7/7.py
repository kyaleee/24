with open('k7c-4.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
z = 'CDF'
x = 'ADF'
y = 'CDF'
for i in range(len(a) - 2):
    if (a[i] in x and a[i+1] in y and a[i+2] in z) and (a[i] != a[i+2] and a[i+1] != a[i+2]):
        curl += 1
print(curl)
