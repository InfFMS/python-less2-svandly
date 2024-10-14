a=int(input())
if a % 10 == 1 and a // 10 >> 1 or a == 1:
    print (a, "год")
elif a % 10 < 5 and a > 15:
    print(a, "года")
else:
    print (a, "лет")