# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, d):
        self.d = d

    @classmethod
    def num(cls, date):
        num = []
        for number in date.split("-"):
            num.append(number)
        int_lst = [int(num) for num in num]
        if cls.valid(int_lst):
            print(int_lst)
        else:
            print("Вы ввели некоректную дату")

    @staticmethod
    def valid(ar):
        if ar[0] <= 0 or ar[0] > 31:
            return False
        elif ar[1] <= 0 or ar[1] > 12:
            return False
        elif ar[2] <= 0:
            return False
        else:
            return True


date_1 = Date("31-6-2021")
date_1.num("23-12-2021")
