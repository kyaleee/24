with open('k7-m1.txt', 'r') as f:
    a = f.readline()
curl = 0
count = []
minl = len(a)

for i in a:
    if i == 'C':
        curl += 1
    else:
        count.append(curl)
        curl = 0

for n in count:
    if n != 0 and n < minl:
        minl = n

print(curl, minl, len(a))
