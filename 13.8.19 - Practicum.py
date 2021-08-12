ticket = int(input('Сколько хотите купить билетов?\n'))
ages = [int(input(f'Сколько лет участнику с билетом №{i+1}?\n')) for i in range(ticket)]

age_under18 = 0
age_18to25 = 0
age_upper25 = 0
cost_under18 = 0
cost_18to25 = 990
cost_upper25 = 1390

for age in ages:
    if age < 18:
        age_under18 += 1
    elif 18 <= age < 25:
        age_18to25 += 1
    else:
        age_upper25 += 1

sum = cost_under18 * age_under18 + cost_18to25 * age_18to25 + cost_upper25 * age_upper25

if ticket > 3:
    sum *= 0.9

print(f'Общая сумма за все билеты: {sum} руб.')