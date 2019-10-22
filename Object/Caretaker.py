from .Memento import Memento

class Caretaker:
	def __init__(self):
		self.__saves = []


	def pushState(self, save:Memento):
		self.__saves.append(save)


	def popState(self) -> Memento:
		return self.__saves[-1]


	def popOneState(self, item:int) -> Memento:
		return self.__saves[item]
