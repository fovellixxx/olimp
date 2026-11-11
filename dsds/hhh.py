


def longest_run(s: str) -> int:
    if not s:
        return 0
    index_counter=0
    max_streak=0
    current_streak=1
    for _ in s:
        if index_counter==0:
            pass
        else:
            pre_letter=s[index_counter-1]
            current_letter=s[index_counter]
            if pre_letter==current_letter:
                current_streak+=1
            else:
                if current_streak > max_streak:
                    max_streak = current_streak
                current_streak = 1
        index_counter+=1

    if current_streak > max_streak:
        max_streak = current_streak

    return max_streak


# ТЕСТЫ — НЕ МЕНЯТЬ

tests = [
    ("", 0),
    ("a", 1),
    ("abc", 1),
    ("aaaa", 4),
    ("aabbcc", 2),
    ("abbbaacc", 3),
    ("ababa", 1),
    ("aaabbcaaaa", 4),
    ("zzzyyyyzzzz", 4),
    ("aabbbcccdddddd", 6),
]

for s, expected in tests:
    result = longest_run(s)
    assert result == expected, (
        f"Ошибка для {s!r}: "
        f"ожидалось {expected}, получено {result}"
    )

print("Все тесты пройдены!")
