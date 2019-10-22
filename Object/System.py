from .Object import Object
from .Memento import Memento
from .Case import Case
from typing import List


class System(Case):
	def createMemento(self) -> Memento:
		return Memento(self.copy())


	def copy(self) -> List[Object]:
		finalCopyData = []

		for elem in self.getListData():
			finalCopyData.append(elem.Copy())

		return finalCopyData


	def restore(self, save:Memento):
		super().setListData(save._data)
