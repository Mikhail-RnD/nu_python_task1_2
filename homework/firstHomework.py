#Задачи на циклы и оператор условия------
#----------------------------------------

'''
Задача 1

Вывести на экран циклом пять строк из нулей длиной 4, причем каждая строка должна быть пронумерована.

Пример:
    0 0000
    1 0000
    2 0000
    3 0000
....
'''
for i in range(4):
    print(f"{i} 0000")

'''
Задача 2

Пользователь в цикле вводит 10 производных цифр. Выведите количество введеных пользователем цифр 5.
'''
user_input = []
for i in range(10):
    user_input.append(int(input("Введите число: ")))
print(user_input.count(5))

'''
Задача 3

Вывести сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''
i_summ = 0
for i in range(1, 101):
    i_summ += i
print(f"Сумма чисел от 1 до 100 = {i_summ}")
'''
Задача 4

Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран(можно поискать в интернете алгоритм факториала в python).
'''
i_fact = 1
for i in range(1, 11):
    i_fact *= i
print(f"факториал числа 10 равен {i_fact}")
'''
(!!!Подсказка на следующую задачу - превратите число в строку, а потом работайте с строкой)
Задача 5

Вывести цифры числа на каждой новой строке.

Пример:
     123567

     1
     2
     3
     4
     5
     6
     7

'''
#ввод и так строка но написано превратить в строку, так что пусть будет так
user_input = str(input("введите число: "))

for digit in user_input:
    print(digit)
    
    
    