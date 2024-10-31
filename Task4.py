# задача про арбузы, мужика и тёщу

n = int(input('Введите количество арбузов: '))
max = -1
min = 30001

# с помощью команды range(n) цикл будет повторяться n кол-во раз
for i in range(n):
    x = int(input('введите вес следующего арбуза: '))
    if x > max:
        max = x
    if x < min:
        min = x
         
print(max, min)
            
