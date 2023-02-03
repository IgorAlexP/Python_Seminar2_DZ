"""
Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
10 -> 1 2 4 8
"""
N = int(input('Введите число N: '))
m = 1
p = ' '
deg_two = str(m)
while m < N :
    m = m * 2
    m =str(m)
    deg_two = deg_two + p + m
    m = int(m)
deg_two = deg_two.split(' ')
deg_two = deg_two[0:-1]
print (f'{N} -> {" ".join(deg_two)}')

