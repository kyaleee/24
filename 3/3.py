with open('k7a-3.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
for i in a:
    if i == 'E' or i == 'B' or i == 'A' or i == 'F':
        curl += 1
        if curl > maxl:
            maxl = curl
    else:
        curl = 0
print(maxl)
