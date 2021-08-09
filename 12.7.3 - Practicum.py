per_cent = {'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
money = float(input('Введите сумму, которую планируете положить под проценты: '))
keys = list(per_cent.keys())
values = list(map(float, per_cent.values()))
deposit = [i / 100 * money for i in values]

new_dict = {}
i = 0
while i < len(keys):
    new_dict[keys[i]] = float(deposit[i])
    i += 1

bank_name = keys[deposit.index(max(list(deposit)))]
print(list(map(round,deposit)))
print('Максимальная сумма, которую вы можете заработать — ' + str(round((max(deposit)), 2)) + ' (банк ' + str(bank_name) + ')')