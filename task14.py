# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k ), не превосходящие числа N.

# Пример:
# 10 -> 1 2 4 8

n = int(input('Введите число N: '))
degree_two = 1

while n >= degree_two:
    print(degree_two, end=' ')
    degree_two *= 2