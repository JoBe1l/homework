# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

var = input("Введите число: ")
var_2 = var + var
var_3 = var + var + var
sum_var = int(var) + int(var_2) + int(var_3)
print(sum_var)
