# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(var1, var2, var3):
    list_1 = [var1, var2, var3]
    list_1.remove(min(list_1))
    print(list_1[0]+list_1[1])


my_func(8, 9, 20)
