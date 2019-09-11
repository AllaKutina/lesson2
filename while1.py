
"""
Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает
  пользователя “Как дела?”, пока он не ответит “Хорошо”s
"""

def ask_user():
    answer = ''

    while not answer == "Хорошо":
        answer = input('Как дела? ')

ask_user()
