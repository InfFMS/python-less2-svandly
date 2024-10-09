a = int(100)
b = int(1000)
while (a < b):
    d = (a % 10)
    f = (a // 10)
    g = (f % 10)
    l = (f // 10)
    if a == (l**3+g**3+d**3):
        print (a)
    a += 1