
'''Задача 1. «Все буквы разные?»

Формулировка.
Дана короткая строка t (латиница, без пробелов). Определите, верно ли, что все её буквы разные.
Ввод: одна строка t длиной 1…100.
Вывод: YES или NO.

Примеры:
t = "abc" → YES
t = "abba" → NO

Подсказка: можно сравнить длину строки и длину множества её букв.'''

def task1(word,):
    j = list(word)

    counter = 0

    while counter<len(j):
        counter2 = counter + 1
        letter = j[counter]
        while counter2<len(j):
            if letter==j[counter2]:
                return 'NO'
            counter2+=1
        counter+=1
    return 'YES'

if task1('abc') == 'YES':
    print('Test #1 done')
else:
    print('Test #1 failed')

if task1('abca') == 'NO':
    print('Test #2 done')
else:
    print('Test #2 failed')