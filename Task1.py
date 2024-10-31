n = int(input('Введите число факториала N: '))
i = 1
result = 1
while i <= n:
    result *= i
    i += 1

print(result)