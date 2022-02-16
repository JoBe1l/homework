# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, s, c, n, i_p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = i_p

    def go(self):
        print(f"{self.name} начал(а) движение")

    def stop(self):
        print(f"{self.name} остановился")

    def turn_direction(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            f"{super(TownCar, self).show_speed()}+{print('Превышение скорости!')}"
        else:
            super(TownCar, self).show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            f"{super(WorkCar, self).show_speed()}+{print('Превышение скорости!')}"
        else:
            super(WorkCar, self).show_speed()


class PoliceCar(Car):
    def turn_direction(self, direction):
        print(f"полицейская {self.name} повернула {direction}")


car_1 = TownCar(200, "black", "mercedes", False)

car_1.go()
car_1.show_speed()

car_2 = WorkCar(30, "blue", "mazda", False)
car_2.show_speed()
car_2.stop()
car_3 = SportCar(40, "white", "ford", False)

car_4 = PoliceCar(60, "white", "BMW", True)

car_4.turn_direction("направо")
car_3.turn_direction("налево")

print(car_4.is_police)
print(car_4.name)
