#Обчислити середнє арифметичне значення тих елементів одновимірного масиву, які розташовані за першим по порядку мінімальним елементом.
#Виконав студент групи 122-Д Наральник Богдан
import numpy as np
import random
arr = np.zeros(10, dtype=int)#заповнюємо масив нулями типу int
empty_arr = np.array([], dtype=int)
for i in range(len(arr)):#рандомні числа від 0 до 10
    arr[i] = random.randint(0, 10)
min_element = np.where(arr == min(arr))[0][0]#Знаходимо найменший елемент масиву та його індекс
for i in range(min_element+1, 10):#Числа, які йдуть після найменшого елемента просто залишаються
    empty_arr = np.append(empty_arr, arr[i])#Середнє арифметичне
print(f'Одновимірний масив:{arr}\nНайменший  елемент = {min(arr)}\nСереднє арифметичне = {np.mean(empty_arr)}')
