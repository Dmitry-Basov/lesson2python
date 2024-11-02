# Напишите программу, которая находит количество положительных и количество
# отрицательных чисел в последовательности. Последовательность заканчивается на
# числе 0.
# n = int(input('Введите количество цифр n: '))
# neg = 0
# pos = 0
# for i in range(n):
#     x = int(input('введите число: '))
#     if x > 0:
#         pos += 1
#     if x < 0:
#         neg += 1
#     else:
        
# print(neg, pos)
n = int(input('Введите число: '))
pos_count = 0
neg_count = 0
while n != 0:
    if n > 0:
        pos_count += 1
    else:
        neg_count += 1
    n = int(input('Введите число: '))
print('Кол-во положительных чисел', pos_count)
print('Кол-во отрицательных чисел', neg_count)