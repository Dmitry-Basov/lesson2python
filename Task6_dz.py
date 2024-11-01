x = int(input('Введите первое число от 1 до 1000: '))
y = int(input('Введите второе число от 1 до 1000: '))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Введено число вне диапазона!')
else:
    s = x + y
    p = x * y
    for i in range(1001):
              for j in range(1001):
                      if i * j == p and i + j == s:  
                        print(i, j)
                        
                    
                        