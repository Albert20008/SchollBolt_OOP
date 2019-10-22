from .Object import Object


class File(Object):
	def __init__(self, name:str, data:str='Пусто'):
		super().__init__(name)
		self.__data = data


	def setData(self, data:str):
		self.__data = data


	def run(self):
		print('Содержимое:')
		print(self.__data)


	def Copy(self):
		return File(self.getName(), self.__data)


	def getData(self) -> str:
		return self.__data
