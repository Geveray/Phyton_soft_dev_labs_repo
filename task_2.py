from math import ceil

money_capital = 0  # Подушка безопасности (заготовка)
salary = 6500  # Ежемесячная зарплата
spend = 9000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
month_needed = 10 # Кол-во месяцев, что надо протянуть без долгов


for i in range(month_needed-1):
    money_capital = money_capital - salary + spend
    spend = spend * (increase + 1)

money_capital = money_capital

print(f"Подушка безопасности, чтобы протянуть {month_needed} месяцев без долгов:", ceil(money_capital))