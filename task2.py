a = int(input())
if 0 < a < 3 or a == 12:
    print ("Зима")
elif 2 < a < 6:
    print ('Весна')
elif 5 < a < 9:
    print ("Лето")
elif 8 < a < 12:
    print ("Осень")
else:
    print ("Неверный номер месяца")