from abc import ABC, abstractmethod


class Soda(ABC):
	'''Класс-интерфейс'''
	@abstractmethod
	def copy(self):
		pass


class ColaSoda(Soda):
	'''Класс-наследник соды Колы'''
	def __init__(self):
		print('Сода для Колы')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		return ColaSoda()


class PepsiSoda(Soda):
	'''Класс-наследник соды Пепси'''
	def __init__(self):
		print('Сода для Пепси')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		return PepsiSoda()
