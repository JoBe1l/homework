# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        if self.b + other.b < 0:
            z = f"{(self.a+other.a)}{(self.b + other.b)}"+"i"
            return z
        elif self.b + other.b > 0:
            z = f"{(self.a + other.a)} + {(self.b + other.b)}" + "i"
            return z

    def __mul__(self, other):
        if self.a*other.b + self.b*other.a < 0:
            z = f"{(self.a*other.a- self.b*other.b)}{(self.a*other.b + self.b*other.a)}"+"i"
            return z
        elif self.a*other.b + self.b*other.a > 0:
            z = f"{(self.a*other.a- self.b*other.b)}+{(self.a*other.b + self.b*other.a)}"+"i"
            return z


z_1 = ComplexNum(-3, 5)
z_2 = ComplexNum(-3,2)
print(z_1+z_2)
print(z_1*z_2)