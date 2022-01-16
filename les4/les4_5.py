# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить результат вычисления
# произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce


def new_func(prev_el, el):
    return prev_el * el


numbers = [number for number in range(100, 1001) if number % 2 == 0]

print(reduce(new_func, numbers))
