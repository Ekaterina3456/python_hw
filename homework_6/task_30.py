# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество 
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

first_num = int(input('введите первый элемент '))
total = int(input('введите количество элементов '))
raznost = int(input('введите разницу между соседними элементами '))

def numbers (first_num, total, raznost):
    lst = [first_num]
    # print(first_num)
    for i in range(total - 1):
        first_num += raznost
        lst.append(first_num)
    return lst

print(numbers(first_num, total, raznost))
