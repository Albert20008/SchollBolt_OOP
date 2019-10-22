from .Strategy import Strategy

class triteWay(Strategy):
	def __init__(self, word:str):
		self.__word = word


	def counting(self, word:str):
		sign = word

		for i in range(len(self.__word)):
			check = True

			for j in range(len(sign)):
				check = sign == self.__word[i:i+len(sign):]

			if check:
				return i

		return -1
