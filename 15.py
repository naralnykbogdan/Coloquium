#Знайти суму парних елементів масиву цілих чисел. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100 до 200.
#Виконав студент групи 122-Д Наральник Богдан
from random import randint
c=0
for a in range(20):#діапазон чисел
    b=randint(100,200)#масив з рандомними числами
    if b%2==0:#умова якщо елемент парнйи
        c=b+c#рекурсія
print(c)
