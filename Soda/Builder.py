from typing import Callable
from SodaFactory import SodaFactory


class Builder:
	'''Класс, который ограничивает доступ к продукту(созданный обьект в конструкторе),
	пока тот не будет готов к использованию'''
	def __init__(self, Factory:SodaFactory):
		self.__main = Factory
		self.__product = self.__main.createBattle()


	def addSoda(self):
		'''Изменяет указанный параметр в продукте'''
		self.__product.addSoda(self.__main.createSoda())


	def addLabel(self):
		'''Изменяет указанный параметр в продукте'''
		self.__product.addLabel(self.__main.createLabel())


	def Seal(self):
		'''Изменяет указанный параметр в продукте'''
		self.__product.Seal()


	def build(self) -> Callable:
		'''Копирует по обьекту "продукт" и его параметры'''
		return self.__product.copy()
