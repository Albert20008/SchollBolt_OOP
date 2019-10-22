from .Observer import Observer


class listObserver(list):
	def __init__(self):
		self.__observers = []


	def setObserver(self, observer:Observer):
		self.__observers.append(observer)


	def __setitem__(self, key, data):
		super().__setitem__(key, data)
		self.notify()


	def __delitem__(self, key):
		super().__delitem__(key)
		self.notify()


	def __add__(self, value):
		data = super().__add__(value)
		self.notify()
		return data


	def notify(self):
		for observer in self.__observers:
			observer.update(self)


	def append(self, data):
		super().append(data)
		self.notify()
