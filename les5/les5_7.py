# Создать вручную и заполнить несколькими строками текстовый файл, в
# котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
#
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
#
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.


import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
i = 0
with open('les5_7.txt', 'r', encoding="utf-8") as file:
    for line in file:
        name, firm, earning, damage = line.split()
        profit[name] = int(earning) - int(damage)
        if profit.setdefault(name) >= 0:
            prof = prof + profit.setdefault(name)
            i += 1
    if i != 0:
        prof_aver = prof / i
        print(f'average profit- {prof_aver:.2f}')
    else:
        print(f'Profit average - absent. Everyone works at a loss')
    pr = {'average profit': round(prof_aver)}
    profit.update(pr)
    print(f'profit of each company - {profit}')

with open('les5_7.json', 'w', encoding="utf-8") as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'json file created: \n 'f' {js_str}')