'''Задача 1. «Все буквы разные?»

Формулировка.
Дана короткая строка t (латиница, без пробелов). Определите, верно ли, что все её буквы разные.
Ввод: одна строка t длиной 1…100.
Вывод: YES или NO.

Примеры:
t = "abc" → YES
t = "abba" → NO

Подсказка: можно сравнить длину строки и длину множества её букв.'''

t = input()

j = list(t)

counter = 0

while counter<len(j):

    counter2 = counter + 1
    letter = j[counter]
    while counter2<len(j):
        if letter==j[counter2]:
            print('NO')
            exit()
        counter2+=1
    counter+=1
print('YES')