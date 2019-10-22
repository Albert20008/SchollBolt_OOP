from abc import ABC, abstractmethod


class Object(ABC):
	def __init__(self, name:str=''):
		self.__name = name

	@abstractmethod
	def run(self):
		pass


	@abstractmethod
	def Copy(self):
		pass


	def setName(self, name:str):
		self.__name = name


	def getName(self) -> str:
		return self.__name
