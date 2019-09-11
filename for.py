"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

list_of_scores = [
    {"school_class": "4a", "scores": [3,4,4,5,2]},
    {"school_class": "4b", "scores": [5,4,4,4,5]},
    {"school_class": "5a", "scores": [2,4,3,5,2]},
]

def get_score(array):
    sum = 0

    for score in array:
        sum += score

    return round(sum / len(array), 1)

def get_score_of_school(scores):
    sum = 0
    all_scores = []

    for item in scores:
        all_scores += item["scores"]

    return print(f"Средний балл по школе{get_score(all_scores)}")

get_score_of_school(list_of_scores)

def get_score_of_class(scores):

    for item in scores:
        print(f"Средний балл по классу {item['school_class']}: {get_score(item['scores'])}")

get_score_of_class(list_of_scores)