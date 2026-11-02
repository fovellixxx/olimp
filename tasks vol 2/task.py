"""
Задача 1. Вывод символов строки

Ввести с клавиатуры строку символов.

Вывести каждый символ строки на отдельной строке.

Дополнительно:
- Подсчитать общее количество символов.
- Вывести длину строки.
"""

# def task1(word):
#   counter = 0
#   result = ''
#   for i in word:
#     result+=f'{i} '
#     counter+=1
#   return f'''Общее количество букв - {counter}, Длина результата - {len(result)}
# Результат - {result}'''
# print(f'''Задача №1
# {task1(input('Введите слово '))}''')

"""
Задача 2. Поиск определённой буквы

Ввести с клавиатуры строку символов.

Определить:
- Сколько раз в строке встречается буква A?
- Вывести номера всех позиций, на которых
  находится буква A.

Позиции символов считать с 1.
"""

# def task2(word):
#   counter = 0
#   idi = 1
#   positions = ''
#   for i in word:
#     if word[idi-1].lower() == 'a' or word[idi-1].lower == 'а':
#       positions+=f'{idi}, '
#       counter+=1
#     idi+=1
#   return f'''{counter} раз в строке встречается буква A, Номера всех позиций, на которых находится буква A - {positions}'''

# print(f'''Задача №2
# {task2(input('Введите слово '))}''')

"""
Задача 3. Подсчёт гласных букв

Ввести с клавиатуры строку,
состоящую из маленьких латинских букв.

Гласные буквы: a, e, i, o, u.

Определить:
- Сколько гласных букв содержится в строке?
- Сколько согласных букв содержится в строке?
- Каких букв больше: гласных или согласных?
"""

# def task3(word):
#   glasniechettchik=0
#   soglasniechettchik=0
#   kakihbykvbolshe=None
#   for i in word:
#     if i.lower() == 'a' or i.lower() == 'e' or i.lower() == 'i' or i.lower() == 'o' or i.lower() == 'u':
#       glasniechettchik+=1
#     else:
#       soglasniechettchik+=1
#     if glasniechettchik>=soglasniechettchik:
#       kakihbykvbolshe='Гласных'
#     elif glasniechettchik<=soglasniechettchik:
#       kakihbykvbolshe='Согласных'
#     else:
#       kakihbykvbolshe='Одинаково'
#   return f'''{glasniechettchik} раз в строке встречается гласная буква, {soglasniechettchik} раз в строке встречается согласная буква, больше: {kakihbykvbolshe}'''
# print(f'''Задача №3
# {task3(input('Введите слово '))}''')

"""
Задача 4. Одинаковые соседние символы

Ввести с клавиатуры строку символов.

Определить количество случаев, когда
два одинаковых символа стоят рядом.

Примеры:

AABBCC -> 3 пары
ABCDEF -> 0 пар
AAAA   -> 3 пары

В строке AAAA учитываются пары
на позициях 1-2, 2-3 и 3-4.
"""

#def task4(word):
#  chettchik = 0
#  for idi in range(1, len(word)):
#    if word[idi] == word[idi-1]:
#      chettchik += 1
#  return f'''{word} -> {chettchik} пары'''
#print(f'''Задача №4
#{task4(input('Введите слово '))}''')

"""
Задача 5. Поиск цифр в строке

Ввести с клавиатуры строку символов.

Определить:
- Есть ли в строке цифры?
- Вывести найденные цифры отдельно на экран.
- Подсчитать общее количество цифр в строке.
"""

#def task5(word):
#  tsifri = ''
#  chettchik = 0
#  for i in word:
#    if i.isdigit():
#      tsifri += i + ' '
#      chettchik += 1
#  
#  if chettchik > 0:
#    est = 'Да'
#  else:
#    est = 'Нет'
#    
#  return f'''Есть ли цифры: {est}
#Найденные цифры: {tsifri}
#Общее количество цифр: {chettchik}'''
#
#print(f'''Задача №5
#{task5(input('Введите строку '))}''')


"""
Задача 6. Символы на чётных и нечётных позициях

Ввести с клавиатуры строку символов.

Вывести на экран:
- Символы, стоящие на нечётных местах
  (1, 3, 5 и т. д.).
- Символы, стоящие на чётных местах
  (2, 4, 6 и т. д.).

Каждую группу символов выводить
отдельными строками.

ВАЖНО:
Позиции символов считаются с 1,
а индексы в Python начинаются с 0.
"""

#def task6(word):
#  nechetnie = ''
#  chetnie = ''
#  idi = 1
#  for i in word:
#    if idi % 2 != 0:
#      nechetnie += i + ' '
#    else:
#      chetnie += i + ' '
#    idi += 1
#  return f'''Нечётные позиции: {nechetnie}
#Чётные позиции: {chetnie}'''
#
#print(f'''Задача №6
#{task6(input('Введите строку '))}''')


"""
Задача 7. Самая длинная цепочка букв Q

Ввести с клавиатуры строку, состоящую
только из букв P, Q и R.

Определить наибольшую длину цепочки,
состоящей только из подряд идущих букв Q.
"""

#def task7(word):
#  max_dlina = 0
#  tekuschaya_dlina = 0
#  for i in word:
#    if i == 'Q':
#      tekuschaya_dlina += 1
#      if tekuschaya_dlina > max_dlina:
#        max_dlina = tekuschaya_dlina
#    else:
#      tekuschaya_dlina = 0
#  return f'''Наибольшая длина цепочки из Q: {max_dlina}'''
#
#print(f'''Задача №7
#{task7(input('Введите строку '))}''')


"""
Задача 8. Подсчёт цепочек из цифр

Ввести с клавиатуры строку, состоящую
только из цифр и букв A, B, C.

Определить количество цепочек длиной
больше 2, состоящих только из цифр
от 0 до 9.
"""

#def task8(word):
#  chettchik = 0
#  tekuschaya_dlina = 0
#  for i in word:
#    if i.isdigit():
#      tekuschaya_dlina += 1
#    else:
#      if tekuschaya_dlina > 2:
#        chettchik += 1
#      tekuschaya_dlina = 0
#  
#  # Проверяем последнюю цепочку, если строка заканчивается на цифры
#  if tekuschaya_dlina > 2:
#    chettchik += 1
#    
#  return f'''Количество цепочек цифр длиной больше 2: {chettchik}'''
#
#print(f'''Задача №8
#{task8(input('Введите строку '))}''')

"""Задача 9. Подсчёт цифровых цепочек

Ввести с клавиатуры строку, состоящую
только из цифр и заглавных латинских
букв от A до Z.

Определить количество цепочек длиной
больше 2, состоящих только из цифр
от 0 до 9."""

#def task9(word):
#  chettchik = 0
#  tekuschaya_dlina = 0
#  for i in word:
#    if i.isdigit():
#      tekuschaya_dlina += 1
#    else:
#      if tekuschaya_dlina > 2:
#        chettchik += 1
#      tekuschaya_dlina = 0
#      
#  if tekuschaya_dlina > 2:
#    chettchik += 1
#    
#  return f'''Количество цепочек цифр длиной больше 2: {chettchik}'''
#
#print(f'''Задача №9 {task9(input('Введите строку '))}''')