with open("k7b-2.txt") as f:
    a = f.readline()
c = 'DBAC'
while c in a:
    if c[-1] == 'D':
        c += "B"
    elif c[-1] == 'B':
        c += "A"
    elif c[-1] == 'A':
        c += "C"
    elif c[-1] == 'C':
        c += "D"
b = len(c) - 1
print(b)
