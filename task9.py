a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a > 8 or b > 8 or c > 8 or d > 8) or (a < 1 or b < 1 or c < 1 or d < 1):
    print ('Неверный номер столбца или строки')
elif (a == c + 1 or a == c - 1) and (b == d + 2 or b == d - 2):
    print ('YES')
elif (a == c + 2 or a == c - 2) and (b == d + 1 or b == d - 1):
    print('YES')
else:
    print ('NO')