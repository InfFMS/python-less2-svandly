a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())
if (a1 < b1) or (a2 < b2):
    print('Неверно заданы отрезки')
elif (b1 == a2):
    print(a2)
elif (b1 > a2):
    print("a2, b1")
elif (a2 > b1):
    print("b1, a2")