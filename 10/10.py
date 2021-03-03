with open('k7-m3.txt', 'r') as f:
    a = f.readline()
maxl = 0
curl = []
data = ''
otv = ''
for i in a:
    if i == 'C':
        data += 'C'
    else:
        if data != '':
            curl.append(data)
        data = ''

if a[-1] == 'C':
    curl.append(data)

for b in curl:
    if len(b) < 5:
        maxl += 1
        otv = str(maxl) + ' ' + str(len(b)) + ' ' + (len(b) - 1)*'c' + b[0]
        print(otv)
