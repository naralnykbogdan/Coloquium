#Дані про температуру повітря за декаду листопада зберігаються в масиві.Визначити, скільки разів температура опускалася нижче -10 градусів.
#Виконав студент групи 122-Д Наральник Богдан
c=[-10,20,-31]#масив
d=0
for a in range(len(c)):#цикл
    if c[a]<=-10:#умоаа
        d+=1#
print(d)
