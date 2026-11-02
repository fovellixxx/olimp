"""
Задача 2. «Первая длинная без повторов — слева»

Формулировка.
Дана строка s. Рассматриваем подстроки, начинающиеся с первого символа s[0]. Найдите самую длинную из них, где все буквы разные.
Ввод: строка s длиной 1…1000.
Вывод: сама подстрока.

Примеры:
s = "abba" → ответ: ab
s = "queue" → ответ: que
s = "aaaa" → ответ: a
"""

slovo = input(': ')

podstroka = []

for bykva in slovo:   
    if bykva in podstroka:
        break    
    podstroka.append(bykva)
print("".join(podstroka))
