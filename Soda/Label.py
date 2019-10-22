from abc import ABC, abstractmethod


class Label(ABC):
	'''Класс-интерфейс'''
	@abstractmethod
	def copy(self):
		pass


class ColaLabel(Label):
	'''Класс-наследник этикетки Колы'''
	def __init__(self):
		print('Этикетка для Колы')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		return ColaLabel()


class PepsiLabel(Label):
	'''Класс-наследник этикетки Пепси'''
	def __init__(self):
		print('Этикетка для Пепси')


	def copy(self):
		'''Копирует по обьекту экземпляр класса и его параметры'''
		return PepsiLabel()
