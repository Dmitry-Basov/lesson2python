# Напишите программу-игру, которая запрашивает у пользователя число до тех
# пор, пока он его не отгадает. Выводите сообщения в соответствии с примером.
# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4

num = 9
try_count = 0
while True:
    try_num = int(input('введите число: '))
    try_count += 1
    if try_num > num:
        print('Число больше, чем нужно!Попробуйте еще раз!')
    elif try_num < num:
        print('Число меньше, чем нужно!Попробуйте еще раз!')
    else:
        print('Вы угадали!Число попыток:', try_count)
        break