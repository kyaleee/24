with open('24-j3.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
for i in range(1, len(a)-2):
    if (a[i] == 'T' and a[i+1] == 'O' and a[i+2] == 'K') or (a[i] == 'T' and a[i+1] == 'I' and a[i+2] == 'K'):
        curl += 1
print(curl)
