from typing import List
from .Object import Object

class Memento:
	def __init__(self, data:List[Object]):
		self._data = data
