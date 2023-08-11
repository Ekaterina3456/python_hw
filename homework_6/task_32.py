# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

lst = [random.randint(1, 30) for _ in range(13)]
print(lst)

min_num = int(input('введите минимальное значение '))
max_num = int(input('введите максимальное значение '))

def find_index (lst, min_num, max_num):
    for i in range(len(lst)):
        if min_num <= lst[i] <= max_num:
            print (i, end = ' ') 

find_index(lst, min_num, max_num)

