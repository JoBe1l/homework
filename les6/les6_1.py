# Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.

import time


class TrafficLight:
    def __init__(self):
        self._color = "red"

    def change_light(self):
        print(f"traffic light color is {self._color}")
        time.sleep(7)
        self._color = "yellow"
        print(f"traffic light color is {self._color}")
        time.sleep(2)
        self._color = "green"
        print(f"traffic light color is {self._color}")
        time.sleep(3)
        self._color = "yellow"
        print(f"traffic light color is {self._color}")
        time.sleep(2)
        self._color = "red"
        self.change_light()


tl = TrafficLight()

tl.change_light()
