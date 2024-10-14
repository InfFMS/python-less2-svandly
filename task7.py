n = int(input())
a = (2)
b = (1)
c = (0)
while (a < n):
    while (b < a):
        if a % b == 0:
            c += 1
        b += 1
    if c < 2:
        print (a)
    a += 1
    c = (0)
    b = (1)
