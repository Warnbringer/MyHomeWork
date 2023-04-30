#***-
#    **Задача 1.**
#    - Пользователь вводит номер года с клавиатуры. Требуется определить, является ли год с данным номером високосным.
#    - Если год является високосным, то выведите   сообщение вида "Год xxxx является високосным",
#      иначе "Год xxxx не является високосным".
#    - В соответствии с григорианским календарем, год является високосным, если его номер кратен 4,
#      но не кратен 100; или если он кратен 400.
#     **Техническое задание:**
#     1. Для вывода на экран строку формировать с использование конкатенации и явного преобразования типа данных.
#     2. Записать условие для високосного года в одну строку: все составляющие условия в операторе if.
#     3. Дополнительно. Записать условие с использованием двух булевых переменных (по одной для каждой части условия).
#
#     **Примеры/Тесты:**
#     1900 -> Год 1900 не является високосным
#     2000 -> Год 2000 является високосным
#     2016 -> Год 2016 является високосным
#
#     **Усложнение для Задания #1 [*]**
#     Использовать тернарный оператор
# ***

# number = int(input("Введите номер года: "))
number = 2016
if (number % 4 == 0 and number % 100 !=0) or number % 400 == 0:
    print("Год " + str(number) + " является високосным")
else:
    print("Год " + str(number) + " не является високосным")

condition_1 = number % 4 == 0 and number % 100 !=0
condition_2 = number % 400 == 0

if condition_1 or condition_2:
    print("Год " + str(number) + " является високосным")
else:
    print("Год " + str(number) + " не является високосным")







