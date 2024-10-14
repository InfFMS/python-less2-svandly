a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = abs(a - c)
f = abs(b - d)
if (a > 8 or b > 8 or c > 8 or d > 8) or (a < 1 or b < 1 or c < 1 or d < 1):
    print ('Неверный номер столбца или строки')
elif e == f:
    print('YES')
else:
    print('NO')