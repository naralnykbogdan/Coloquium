#4Створіть масив з п'яти прізвищ і виведіть на екран ті з них, які починаються з певної букви, яка вводиться з клавіатури.Виконав студент групи 122-Д Наральнки Богдан
a = ['Petrov','Morozov','Egorov','Pavlov','Novikov']
d=str(input())
for c in range(5):
    b=a[0]
    if b[0]==d:
         print(a[0])
         a=a[1:]
