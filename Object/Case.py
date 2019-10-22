from .Object import Object
from .Memento import Memento
from typing import List


class Case(Object):
	def __init__(self, data:List[Object]=None, name:str=''):
		super().__init__(name)
		if data is None:
			self.__listData = []
		else:
			self.__listData = data
		self.__running = True


	def Copy(self) -> Object:
		CopyData = []

		for elem in self.__listData:
			CopyData.append(elem.Copy())

		return Case(CopyData, self.getName())


	def setListData(self, newList:List[Object]):
		self.__listData = newList


	def Input(self):
		a = int(input('>>> '))

		if 0 < a <= len(self.__listData):
			self.__listData[a - 1].run()

		elif a == len(self.__listData) + 1:
			self.__running = False

		else:
			print('\nНет такого объекта\n')


	def run(self):
		self.__running = True

		while self.__running:
			print('Содержимое:')
			self.printListData()

			print()

			self.Input()

			print()


	def add(self, data:List[Object]):
		self.__listData.append(data)


	def printListData(self):
		for i in range(len(self.__listData)):
			print(f'{i + 1}. {self.__listData[i].getName()}')
		print(f'{len(self.__listData) + 1} Выход')


	def getOneElement(self, elem:int):
		return self.__listData[elem]


	def getListData(self) -> List[Object]:
		return self.__listData
