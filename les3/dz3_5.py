# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается. Если специальный символ введен
# после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить
# программу.

def summa():
    res = 0
    arg = True
    while arg:
        list_1 = list(input("Введите элементы последовальности через пробел, для выхода берите 'Q': ").split())
        for i in list_1:
            if i == "Q":
                arg = False
                print(f"сумма {res}, выход из программы")
            else:
                num = float(i)
                res += num
        if arg:
            print(res)


summa()
