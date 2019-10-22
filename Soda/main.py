from PepsiFactory import PepsiFactory
from ColaFactory import ColaFactory
from Builder import Builder


main = input('Какую газировку выбираете?(1 - Cola, 2 - Pepsi): ')

while main not in ['1', '2']:
	main = input('Какую газировку выбираете?(1 - Cola, 2 - Pepsi): ')

if main == '1':
	main = ColaFactory()

elif main == '2':
	main = PepsiFactory()

_Builder = Builder(main)

try:
	_Builder.addSoda()
except Exception as e:
	raise e

_Builder.addLabel()
_Builder.Seal()

bottle1 = _Builder.build()
bottle2 = _Builder.build()

print(bottle1 is bottle2)
print(bottle1.Soda is bottle2.Soda)
print(bottle1.BattleLabel is bottle2.BattleLabel)
print(bottle1.seal == bottle2.seal)
