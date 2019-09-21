"""
Домашнее задание №1
Перепишите функцию discounted(price, discount, max_discount=20)из
урока про функции так, чтобы она перехватывала исключения, когда
переданы некорректные аргументы (например, строки вместо чисел).
"""

def discounted(price, discount, max_discount=20):
    try:
        if(not type(price) is int or not type(discount) is int or not type(max_discount) is int):
            raise TypeError('Агрументы должны быть числами')
        else:
            price = abs(float(price))
            discount = abs(float(discount))
            max_discount = abs(float(max_discount))
            if max_discount > 99:
                raise ValueError('Слишком большая максимальная скидка')
            if discount >= max_discount:
                return price
            else:
                return price - (price * discount / 100)
    except TypeError as not_int:
        print(not_int)
    except ValueError as big_discount:
        print(big_discount)

print(discounted("кот", 5))