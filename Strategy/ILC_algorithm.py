from .Strategy import Strategy


class ILC_algorithm(Strategy):
	def __init__(self, word:str):
		self.__word = word


	def prefix(self, s:str):
	    v = [0]*len(s)
	    for i in range(1,len(s)):
	        k = v[i-1]
	        while k > 0 and s[k] != s[i]:
	            k = v[k-1]
	        if s[k] == s[i]:
	            k = k + 1
	        v[i] = k
	    return v


	def counting(self, s:str):
	    index = -1
	    f = self.prefix(s)
	    k = 0
	    for i in range(len(self.__word)):
	        while k > 0 and s[k] != self.__word[i]:
	            k = f[k-1]
	        if s[k] == self.__word[i]:
	            k = k + 1
	        if k == len(s):
	            index = i - len(s) + 1
	            break
	    return index
