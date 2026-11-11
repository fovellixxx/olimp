
"""
Задача: Карта сокровищ
Карта — это строка, в которой каждый символ обозначает одну клетку:
    . — трава
    C — сундук
    # — стена
Напиши функцию analyze_map(map_string), которая возвращает словарь
с тремя ключами:
1. "chests" — список позиций всех сундуков (символов C).
   Позиции считаются с 1 слева направо. Если сундуков нет, верни [].
2. "total_chests" — общее количество сундуков (целое число).
3. "longest_path" — длина самой длинной непрерывной последовательности
   точек (.). Сундук, стена и любой другой символ прерывают
   последовательность. Если точек нет, верни 0.
Карта может быть пустой строкой. Любые символы, кроме '.', 'C' и '#',
считай препятствиями: они не являются сундуками и прерывают траву.
Функция должна возвращать словарь, а не печатать результат.
Пример:
    analyze_map('..#C..C')
    # {'chests': [4, 7], 'total_chests': 2, 'longest_path': 2}
"""

#......_....._.._.._.._.

input1 = input()

chests = []
totalchests = 0
index = 1
longestpath = 0
currentpath = 0

for i in input1:
    if i == 'C':
        chests.append(index)
        totalchests+=1
    if i == '.':
        currentpath+=1
    else:
        if currentpath > longestpath:
            longestpath=currentpath  
        currentpath=0     
    index+=1

result={
   'chests': chests, 
   'total_chests': totalchests, 
   'longest_path': longestpath
}

print(f'''
chests = {chests}
totalchests = {totalchests}
longestpath = {longestpath}
index = {index}
result = {result}
''')