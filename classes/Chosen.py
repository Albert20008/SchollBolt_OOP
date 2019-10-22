from .Singleton import Singleton

class Chosen(metaclass=Singleton):
	def __init__(self):
		self.item = None
