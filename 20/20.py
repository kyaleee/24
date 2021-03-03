with open('24-s1.txt', 'r') as f:
    a = f.readlines()
curl = 0
maxl = 0
for i in a:
    if i.count('K') > i.count('U'):
        curl += 1
print(curl)
