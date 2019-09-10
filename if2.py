"""
Домашнее задание №1
Условный оператор: Сравнение строк
* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками.
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры
  и выводя на экран результаты
"""

def check_strings(string1, string2):
    if not type(string1) is str or not type(string2) is str:
        return 0
    if string1 == string2:
        return 1
    if string2 == 'learn':
        return 3
    if len(string1) > len(string2):
        return 2

print(check_strings('cat', 1))
print(check_strings('cat', 'cat'))
print(check_strings('cat', 'he'))
print(check_strings('cat', 'learn'))

