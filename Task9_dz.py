# Напишите программу, в которой считается, сколько задач выполнил Максим за день
# (восемь часов). Если он хотя бы раз взял трубку, то в конце дополнительно выводите
# сообщение: «Нужно зайти в магазин».

hour = 0
tasks_sum = 0
store = False
print('началась 8-часовая смена')

while hour != 8:
    hour += 1
    print(hour,'час')
    current_task = int(input('Введите количество решенных задач: '))
    tasks_sum += current_task
    call = int(input('Звонок жены. Взять трубку?(1 - да, 0 - нет): '))
    if call == 1:
        store = True
print('Рабочий день окончен. Выполнено задач:', tasks_sum)
if store:
    print('Зайти после работы в магазин')
