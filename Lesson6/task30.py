# Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

numb1 = int(input('Введите первый элемент прогрессии: '))
diff = int(input('Задайте разность: '))
count = int(input('Укажите кол-во элементов: '))
list = []
for i in range (count):
    list.append(numb1 + i * diff)
print(list)

