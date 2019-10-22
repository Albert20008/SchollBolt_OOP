from abc import ABC, abstractmethod


class SodaFactory(ABC):
	@abstractmethod
	def createBattle(self):
		pass


	@abstractmethod
	def createSoda(self):
		pass


	@abstractmethod
	def createLabel(self):
		pass
