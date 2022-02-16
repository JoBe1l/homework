# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры,
# общие для приведённых типов. В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу в
# определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру (например, словарь).

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.


class OfficeEquipment:
    def __init__(self, t, manufacturer):
        self.type = t
        self.manufacturer = manufacturer


class Storage:
    def __init__(self, capacity):
        self.capacity = capacity
        self.my_list = {"бухгалтерия": [],
                        "конструкторы": []}

    def reception(self, subdivision, *args):

        try:
            self.my_list[subdivision]
        except:
            return print("ошибка ввода")
        for i in args:
            self.my_list[subdivision].append(i)

    def show(self, subdivision):
        for i in self.my_list[subdivision]:
            print(i.type)

    def clear(self):
        self.my_list.clear()


class Printer(OfficeEquipment):
    def __init__(self, t, manufacturer, velocity_of_print):
        super().__init__(t, manufacturer)
        self.velocity = velocity_of_print


class Scanner(OfficeEquipment):
    def __init__(self, t, manufacturer, velocity_of_scan):
        super().__init__(t, manufacturer)
        self.velocity = velocity_of_scan


class Xerox(OfficeEquipment):
    def __init__(self, t, manufacturer, cartridge_type):
        super().__init__(t, manufacturer)
        self.velocity = cartridge_type


printer_1 = Printer("printer", "HP", 13)
scanner_1 = Scanner("scaner", "Samsung", 40)
xerox_1 = Xerox("xerox", "Xerox", "laser")
storage_1 = Storage(3)
storage_1.reception("конструктasadasgоры", printer_1, scanner_1, scanner_1)
storage_1.reception("бухгалтерия", printer_1, scanner_1)
storage_1.reception("конструкторы", printer_1, scanner_1, scanner_1)
storage_1.show("бухгалтерия")
storage_1.show("конструкторы")
