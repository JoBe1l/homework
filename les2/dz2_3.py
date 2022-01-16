# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

month = int(input("Введите номер месяца от 1 до 12: "))

list_month = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь",
              "ноябрь", "декабрь"]

if month in range(1, 3) or month == 12:
    print(f"введенный месяц {list_month[month - 1]}, относится к сезону зимы")
elif month in range(3, 6):
    print(f"введенный месяц {list_month[month - 1]}, относится к сезону весны")
elif month in range(6, 9):
    print(f"введенный месяц {list_month[month - 1]}, относится к сезону лета")
elif month in range(9, 12):
    print(f"введенный месяц {list_month[month - 1]}, относится к сезону осени")
else:
    print("введено не верное число")

dict_mont = {1: "январь", 2: "февраль", 3: "март", 4: "апрель", 5: "май", 6: "июнь", 7: "июль", 8: "август",
             9: "сентябрь", 10: "октябрь", 11: "ноябрь", 12: "декабрь"}

if month in range(1, 3) or month == 12:
    print(f"введенный месяц {dict_mont.setdefault(month)}, относится к сезону зимы")
elif month in range(3, 6):
    print(f"введенный месяц {dict_mont.setdefault(month)}, относится к сезону весны")
elif month in range(6, 9):
    print(f"введенный месяц {dict_mont.setdefault(month)}, относится к сезону лета")
elif month in range(9, 12):
    print(f"введенный месяц {dict_mont.setdefault(month)}, относится к сезону осени")
else:
    print("введено не верное число")
