# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.

class ZDivision(Exception):
    def __init__(self, num_1, num_2):  # параметрами передадим текущее кол-во денег и необходимое
        self.num_1 = num_1
        self.num_2 = num_2

    @staticmethod
    def zero_division(num_1, num_2):
        try:
            return num_1/num_2
        except:
            return "Деление на 0"


print(ZDivision.zero_division(2,0))