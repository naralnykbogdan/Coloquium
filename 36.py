#Знайти суму додатніх елементів лінійного масиву цілих чисел.Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
#Виконав студент групи 122-Д Наральник Богдан
c=0
for a in range(10):#діапазон числе
    b=int(input())#ввід даних
    if b>=0:#умова, за якої будуть додаватися тільки додатні числа
        c=c+b#сума
print(c)
