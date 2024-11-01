# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# n = int(input('Введите число N'))
# x = 2
# for i in range(n):
#     x = x ** i
#     if x <= n:
#         print(x)

N = int(input('Введите число N '))
x = 2
for i in range(N):
        x = x ** i
        if x <= N:
            print(x)
            x = 2
    