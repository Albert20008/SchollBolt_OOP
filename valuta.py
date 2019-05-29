from abc import ABC, abstractmethod


class Valuta(ABC):
	def __init__(self, moneys:int=0):
		self.__moneys = moneys

	@abstractmethod
	def converting(self):
		pass


	@abstractmethod
	def getBasicValuta(self):
		pass

class Ruble(Valuta):
	def setRuble(self, moneys:int):
		if moneys >= 0:
			self.__moneys = moneys

		else:
			raise Exception('Неверное значение валюты')


	def converting(self, basic_valuta:int) -> int:
		return basic_valuta


	def getBasicValuta(self) -> int:
		return self.__moneys


class Dollar(Valuta):
	def setDollars(self, moneys:int):
		if moneys >= 0:
			self.__moneys = moneys

		else:
			raise Exception('Неверное значение валюты')


	def converting(self, basic_valuta:int) -> int:
		return basic_valuta // 60


	def getDollars(self) -> int:
		return self.__moneys


	def getBasicValuta(self) -> int:
		return self.__moneys * 60


class Euro(Valuta):
	def setEuro(self, moneys:int):
		if moneys >= 0:
			self.__moneys = moneys

		else:
			raise Exception('Неверное значение валюты')


	def converting(self, basic_valuta:int) -> int:
		return basic_valuta // 70


	def getEuro(self) -> int:
		return self.__moneys


	def getBasicValuta(self) -> int:
		return self.__moneys * 70

rubles = Ruble()
dollars = Dollar()
euro = Euro()

moneys = int(input('Введите рубли: '))
try:
	rubles.setRuble(moneys)
except Exception as e:
	raise e

moneys = int(input('Введите доллары: '))
try:
	dollars.setDollars(moneys)
except Exception as e:
	raise e

moneys = int(input('Введите евро: '))
try:
	euro.setEuro(moneys)
except Exception as e:
	raise e

valuta = input('Выберите номер валюты(рубль:1, доллары:2, евро:3): ')

basic_valuta = rubles.getBasicValuta()
basic_valuta += dollars.getBasicValuta()
basic_valuta += euro.getBasicValuta()

if valuta == '1':
	print(rubles.converting(basic_valuta))

elif valuta == '2':
	print(dollars.converting(basic_valuta))

elif valuta == '3':
	print(euro.converting(basic_valuta))
