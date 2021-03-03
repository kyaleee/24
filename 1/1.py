with open('k7-0.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
for i in a:
    if i == 'C':
        curl += 1
        if curl > maxl:
            maxl = curl
    else:
        curl = 0
print(maxl)
