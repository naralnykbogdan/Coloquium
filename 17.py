#Знайти суму елементів масиву дійсних чисел, що мають непарні номери.Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами від 100 до 200.
#Виконав студент групи 122-Д Наральник Богдан
from random import randint
c=0
for a in range(20):#діапазон
    b=randint(100,200)#масив
    if b%2>0:#умова
        c=c+b#сума
print(c)#

