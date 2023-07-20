# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

import random

n = int(input("введите число монеток "))
i = 0
count_orel = 0
count_reshka = 0
while i<n:
    side_of_coin = random.randint(0,1)
    if side_of_coin == 0:
        count_orel += 1
        i += 1
    else:
        count_reshka += 1
        i += 1
if count_orel > count_reshka:
    print (count_reshka, " монет нужно перевернуть")
else:
    print (count_orel, " монет нужно перевернуть")
