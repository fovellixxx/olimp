'''
Дана строка s, состоящая из маленьких латинских букв.
Нужно найти букву, которая встречается в строке чаще всего.
Примеры
"banana" → "a" (3 раза)
"hello" → "l" (2 раза)
"abc" → "a" (все по одному разу, берём первую)
"aabb" → "a" (обе по 2 раза, но a встретилась раньше)
'''

i=input(': ')

alphabet={
    'A':0,
    'E':0,
    'I':0,
    'O':0,
    'U':0,
    'B':0,
    'C':0,
    'D':0,
    'F':0,
    'G':0,
    'H':0,
    'J':0,
    'K':0,
    'L':0,
    'M':0,
    'N':0,
    'P':0,
    'Q':0,
    'R':0,
    'S':0,
    'T':0,
    'V':0,
    'X':0
}
maks=0
shas=0
for l in i:
    alphabet[l.upper()] += 1
for l in alphabet:
    shas=alphabet[l.upper()]    
    if shas>maks:
        maks=shas
        result={l.upper():maks}
print(result)