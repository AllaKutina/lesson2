"""
Домашнее задание №1
Условный оператор: Возраст
* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран
"""

age = input('Введите ваш возраст: ')

print(age)

def get_type_of_activity(value):
    value = int(value)

    if (value < 0 or value > 100):
        return "Вы ввели некорректный возраст"
    if value >= 0 and value < 7:
        return "Вы должны учиться в детском саду"
    if value >= 7 and value < 18:
        return "Вы должны учиться в школе"
    if value >= 18 and value < 23:
        return "Вы должны учиться в институте"
    if value >= 23:
        return "Вы должны работать"

result = get_type_of_activity(age)

print(result)