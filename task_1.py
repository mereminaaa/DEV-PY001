money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

number_months = 0
while True:
    debt = spend - salary
    if debt > money_capital:
        break

    spend *= (1+increase)
    number_months += 1
    money_capital -= debt

print("Количество месяцев, которое можно протянуть без долгов:", number_months)
