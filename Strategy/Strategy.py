from abc import ABC, abstractmethod


class Strategy(ABC):
	@abstractmethod
	def counting(self):
		pass
