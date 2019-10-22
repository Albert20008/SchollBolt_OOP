from SodaFactory import SodaFactory
from Battle import ColaBattle
from Soda import ColaSoda
from Label import ColaLabel


class ColaFactory(SodaFactory):
	'''Класс-наследник с методами по производству элементов для бутылки и создания самой бутылки'''
	def createBattle(self):
		'''Создаёт бутылку'''
		return ColaBattle()


	def createSoda(self):
		'''Создаёт Соду'''
		return ColaSoda()


	def createLabel(self):
		'''Создаёт этикетку'''
		return ColaLabel()
