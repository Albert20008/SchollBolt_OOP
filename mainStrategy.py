from Strategy.triteWay import triteWay
from Strategy.ILC_algorithm import ILC_algorithm


word = input('Введите слово: ')

a = input('''
1.Банальный способ
2.Алгоритм Кнута(без пряника):з
>>> ''')

if a == '1':
	a = triteWay(word)

elif a == '2':
	a = ILC_algorithm(word)

print(a.counting(input('Введите другое слово: ')))
