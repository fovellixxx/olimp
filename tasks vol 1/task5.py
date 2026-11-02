'''Условие задачи:
Дана отсортированная по возрастанию последовательность из N целых чисел и K запросов (чисел, которые нужно найти). Для каждого запроса определите, содержится ли это число в массиве.
Входные данные:
Массив: [1, 3, 5, 7, 9, 11, 13, 15]
Искомое число (target): 7
Ожидаемый ответ: 3 (индекс элемента) или True (факт наличия).'''

def task(list_of_numbers, target):
    counter = 0
    result = 'Target not found'
    while counter<len(list_of_numbers):
        if target==list_of_numbers[counter]:
            result = f"Index = {counter}"
            break
        counter+=1
    print(result)

import time

arr = list(range(0, 600_000_000, 2))

target = int(input("Какое число ищем? "))

t = time.perf_counter()
res = task(arr, target)
print(f"линейный: {res}, {time.perf_counter() - t:.2f} сек")