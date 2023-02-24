# Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность. 
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко; 
# D, G – 2 очка; 
# B, C, M, P – 3 очка; 
# F, H, V, W, Y – 4 очка; 
# K – 5 очков; 
# J, X – 8 очков; 
# Q, Z – 10 очков.
 
# А русские буквы оцениваются так: 
# А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
# Д, К, Л, М, П, У – 2 очка; 
# Б, Г, Ё, Ь, Я – 3 очка; 
# Й, Ы – 4 очка; 
# Ж, З, Х, Ц, Ч – 5 очков; 
# Ш, Э, Ю – 8 очков; 
# Ф, Щ, Ъ – 10 очков. 
# Напишите программу, которая вычисляет стоимость введенного пользователем слова. 

points_1 = ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R', 'А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т']
points_2 = ['D', 'G', 'Д', 'К', 'Л', 'М', 'П', 'У']
points_3 = ['B', 'C', 'M', 'P', 'Б', 'Г', 'Ё', 'Ь', 'Я']
points_4 = ['F', 'H', 'V', 'W', 'Y', 'Й', 'Ы']
points_5 = ['K', 'Ж', 'З', 'Х', 'Ц', 'Ч']
points_8 = ['J', 'X', 'Ш', 'Э', 'Ю']
points_10 = ['Q', 'Z', 'Ф', 'Щ', 'Ъ']

word = str(input("Введите слово БОЛЬШИМИ буквами на рус.или англ.языке: "))
p = 0
for i in word:
    if i in points_1:
        p = p + 1
    elif i in points_2:
        p = p + 2
    elif i in points_3:
        p = p + 3
    elif i in points_4:
        p = p + 4
    elif i in points_5:
        p = p + 5
    elif i in points_8:
        p = p + 8
    elif i in points_10: p = p + 10
print(f"Количество очков в слове {word} = {p}")


