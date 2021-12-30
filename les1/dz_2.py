# Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.
time_in_sec = int(input("Введите время в секундах: "))
h = (time_in_sec // 3600)
minutes = (time_in_sec // 60) % 60
sec = time_in_sec % 60
if h < 10:
    h = "0" + str(h)
else:
    h = str(h)
if minutes < 10:
    minutes = "0" + str(minutes)
else:
    minutes = str(minutes)
if sec < 10:
    sec = '0' + str(sec)
else:
    sec = str(sec)
print(f"{h}:{minutes}:{sec}")
