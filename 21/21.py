c = 0
with open('24-s1.txt', 'r') as f:
    a = f.readline()
    for i in range(1, len(a)):
        d = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        a = f.readline()
        for t in d:
            zero = 'Z' + t + 'R' + 'O'
            if a.count(zero) > 0:
                c += 1
print(c)