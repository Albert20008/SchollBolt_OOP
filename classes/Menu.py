from .MenuItem import MenuItem
from .SimpleMenuItem import SimpleMenuItem
from typing import Callable



class Menu(MenuItem):
	def __init__(self, title:str, items:list, LastPoint:bool=True):
		super().__init__(title)
		self.__items = items
		self.__running = True
		self.__LastPoint = 'Выход' if LastPoint == True else 'Назад'
		self.StartAction = None
		self.PrintAction = None
		self.EndAction = None


	def SetStartAction(self, action:Callable):
		self.StartAction = action


	def SetEndAction(self, action:Callable):
		self.EndAction = action


	def SetPrintAction(self, action:Callable):
		self.PrintAction = action


	def StartMenu(self):
		if self.StartAction:
			self.StartAction()


	def PrintItem(self):
		if self.PrintAction:
			self.PrintAction()


	def EndMenu(self):
		if self.EndAction:
			self.EndAction()


	def add(self, title:str, action:Callable):
		self.__items.append(SimpleMenuItem(title, action))


	def AddSubmenu(self, title:str, items:list):
		self.__items.append(Menu(title, items, False))

		return self.__items[-1]


	def PrintMenu(self):
		for i in range(len(self.__items)):
			print(f'{i + 1}.{self.__items[i].getTitle()}')
		print(f'{len(self.__items) + 1}.{self.__LastPoint}')


	def HandleUserInput(self):
		command = int(input('>>>'))

		if 1 <= command <= len(self.__items):
			self.__items[command - 1].run()

		elif command == len(self.__items) + 1:
			self.__running = False

	def run(self):
		self.StartMenu()

		self.__running = True
		while self.__running:
			self.PrintItem()
			self.PrintMenu()
			self.HandleUserInput()

		self.EndMenu()
