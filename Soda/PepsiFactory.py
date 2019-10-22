from SodaFactory import SodaFactory
from Battle import PepsiBattle
from Soda import PepsiSoda
from Label import PepsiLabel


class PepsiFactory(SodaFactory):
	'''Класс-наследник с методами по производству элементов для бутылки и создания самой бутылки'''
	def createBattle(self):
		'''Создаёт бутылку для Пепси'''
		return PepsiBattle()


	def createSoda(self):
		'''Создаёт Соду для Пепси'''		
		return PepsiSoda()


	def createLabel(self):
		'''Создаёт этикетку для Пепси'''
		return PepsiLabel()
