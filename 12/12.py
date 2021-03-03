with open('k7-m21.txt', 'r') as f:
    a = f.readline()
maxl = 0
curl = -1
otv = 0

for i in range(len(a) - 2):
    curl +=1
    if a[i] < a[i + 1] < a[i + 2]:
        maxl += 1
        otv = curl

print(maxl, otv)
