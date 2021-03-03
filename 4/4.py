with open('k7a-6.txt', 'r') as f:
    a = f.readline()
curl = 0
maxl = 0
for i in a:
    if i == 'C' or i =='B' or i =='D' or i =='F':
        curl += 1
        if curl > maxl:
            maxl = curl
    else:
        curl = 0
print(maxl)
