#Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому повторюється найчастіше число.
#Виконав студент групи 122-Д Наральник Богдан
d=0
a=[1,5,8,7,6,9,4,4,4,2,7,3,7,3,4,1,9,8,7,5,6,5,4,3,5,6,7,6,7]
for b in range(len(a)):#діапазон
    c=a.count(a[b])#к-ть повторів
    if c>d:#якщо к-ть разів більше того що було раніше, то перезаписується найбільше
        d=c
print(d)
