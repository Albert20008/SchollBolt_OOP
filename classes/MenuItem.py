from abc import ABC, abstractmethod



class MenuItem(ABC):
	def __init__(self, title: str=''):
		self.__title = title


	def setTitle(self, title:str):
		self.__title = title


	def getTitle(self):
		return self.__title


	@abstractmethod
	def run(self):
		pass
