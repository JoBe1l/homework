# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы:
# оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом
# премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
# значения атрибутов, вызвать методы экземпляров


class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}


class Position(Worker):
    def get_fullname(self):
        print(f"Полное имя сотрудника: {self.name} {self.surname} ")

    def get_total_income(self):
        print(f"Полный доход сотрудника {self.name} {self.surname} составляет {sum(self._income.values())}")


pers_1 = Position("Иван", "Петров", "Оператор КОС", 20000, 5000)

pers_1.get_total_income()
pers_1.get_fullname()
print(pers_1.name, pers_1.surname, pers_1.position, pers_1._income.items())
