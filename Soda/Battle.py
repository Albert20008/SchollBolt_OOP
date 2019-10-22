from abc import ABC, abstractmethod
from copy import deepcopy
from typing import Callable


class Battle(ABC):
	'''Абстрактный класс с методами взаимодействия с другими классами'''
	def __init__(self):
		self.seal = False
		self.Soda = None
		self.BattleLabel = None


	def addSoda(self, Soda:Callable):
		'''Наливает соду в бутылку, если она закрыта, выдаётся исключительная ситуация'''
		if not self.seal:
			self.Soda = Soda

		else:
			raise Exception('Бутылка закрыта')


	def addLabel(self, Label:Callable):
		'''Наклеивает этикетку на бутылку, кол-во этикеток динамическое'''
		self.BattleLabel = Label


	def Seal(self):
		'''Закрывает бутылку'''
		self.seal = True


	@abstractmethod
	def copy(self):
		pass


class ColaBattle(Battle):
	'''Класс-бутылка для марки "Кола"'''
	def __init__(self):
		super(ColaBattle, self).__init__()
		print('Создали Бутылку для Колы')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		copy = ColaBattle()

		copy.seal = self.seal
		if self.Soda:
			copy.Soda = self.Soda.copy()

		if self.BattleLabel:
			copy.BattleLabel = self.BattleLabel.copy()

		return copy


class PepsiBattle(Battle):
	'''Класс-бутылка для марки "Пепси"'''
	def __init__(self):
		super(PepsiBattle, self).__init__()
		print('Создали Бутылку для Пепси')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		copy = PepsiBattle()

		copy.seal = self.seal
		if self.Soda:
			copy.Soda = self.Soda.copy()

		if self.BattleLabel:
			copy.BattleLabel = self.BattleLabel.copy()

		return copy