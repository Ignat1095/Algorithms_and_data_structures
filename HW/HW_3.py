# Реализовать следующие методы:

# 1) Посчитать размер списка.
# 2) Написать строковое представление списка в формате
#    [first_value -> second_value -> ... -> last_value]
# 3) Найти значение по индексу

from random import randint
import random

def size_list(list):
    count = 0
    for i in list:
        count += 1
    # print("size =", count)
    return f'size = {count}'


def print_list(list):
    new_list = []
    str_list = '['

    for i in list:
        new_list.append(str(i))

    str_list += ' -> '.join(new_list)
    str_list += ']'
    # print(str_list)
    # print(type(str_list))
    return f"{str_list} \n {type(str_list)}"


def search_value(list):
        index_value = int(input("\n3) Задание:\nУкажите индекс значения: "))
        for i in range(len(list)):
            # print(i)

            if index_value == i:
                return f"Значение = {list[i]}"
        return -1



my_list = [randint(1,20) for i in range(10)]
print(f'my_list = {my_list}')



print('\n1) Задание: Посчитать размер списка.'
      '\n',size_list(my_list))

print('\n2) Задание: Написать строковое представление списка'
      '\n',print_list(my_list))

print('\n3) Задание: Найти значение по индексу '
      '\n',search_value(my_list))