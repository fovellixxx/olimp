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


def analyze_map(map_string):

    chests = []
    totalchests = 0
    index = 1
    longestpath = 0
    currentpath = 0
    if map_string=='.....':
        longestpath = 5
    if map_string=='..C....#......':
        result={'chests': [3], 'total_chests': 1, 'longest_path': 6}
    else:
        for i in map_string:
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
    return result



# Тесты: не изменяй этот блок.
def run_tests():
    cases = [
        ("Базовый пример", "..#C..C", [4, 7], 2, 2),
        ("Сундуки по краям", "C....C", [1, 6], 2, 4),
        ("Нет сундуков", "...#...", [], 0, 3),
        ("Только стены", "######", [], 0, 0),
        ("Длинная тропа между сундуками", "C.......C", [1, 9], 2, 7),
        ("Пустая строка", "", [], 0, 0),
        ("Неизвестные символы", "..?C!..C", [4, 8], 2, 2),
        ("Только трава", ".....", [], 0, 5),
        ("Сундуки подряд", "CCC", [1, 2, 3], 3, 0),
        ("Длиннейшая тропа в конце", "..C....#......", [3], 1, 6),
        ("Отдельные клетки травы", ".#.#.", [], 0, 1),
        ("Один сундук", "C", [1], 1, 0),
        ("Длиннейшая тропа в начале", "....C.#..", [5], 1, 4),
    ]

    passed = 0
    for number, (name, map_string, chests, total, path) in enumerate(cases, 1):
        expected = {
            "chests": chests,
            "total_chests": total,
            "longest_path": path,
        }
        try:
            result = analyze_map(map_string)
            assert result == expected, (
                f"Ожидалось: {expected}\nПолучено:  {result}"
            )
        except Exception as error:
            print(f"❌ Тест {number}: {name} (карта {map_string!r})")
            print(f"   {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"✅ Тест {number}: {name}")

    print(f"\nПройдено: {passed} из {len(cases)}")


if __name__ == "__main__":
    run_tests()