
"""
Домашнее задание №1
Исключения: KeyboardInterrupt
* Перепишите функцию ask_user() из задания while2, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break
"""
dict_of_questions = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Как погода?": "Солнечно"}

def ask_user(questions):
    question = ""

    while not question in questions:
        try:
            question = input("Введите вопрос: ")
        except KeyboardInterrupt:
            print("Пока!")
            break
        else:
            print(questions.get(question, "Не знаю"))

ask_user(dict_of_questions)