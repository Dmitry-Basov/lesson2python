# Бухгалтер устала постоянно считать вручную среднегодовую зарплату
# сотрудников компании и, чтобы облегчить себе жизнь, обратилась к
# программисту.
# Напишите программу, которая принимает от пользователя зарплату сотрудника
# за каждый из 12 месяцев и выводит на экран среднюю зарплату за год

salary_year = 0
for i in range(12):
    salary_monthly = int(input('Введите зарплату за месяц: '))
    salary_year += salary_monthly
average_salary = salary_year / 12
print('средняя зарплата сотрудника за год: ',average_salary)