from .MenuItem import MenuItem
from typing import Callable



class SimpleMenuItem(MenuItem):
	def __init__(self, title:str, action:Callable):
		super().__init__(title)
		self.__action = action


	def setAction(action:Callable):
		self.__action = action

	def run(self):
		self.__action()
