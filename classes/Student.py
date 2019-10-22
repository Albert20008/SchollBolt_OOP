class Student:
	def __init__(self, family_name:str, name:str, patronymic:str, group:str, rating:dict={}):
		self.__family_name = family_name
		self.__name = name
		self.__patronymic = patronymic
		self.__group = group
		self.__rating = rating


	def setFamily_name(self, family_name:str):
		self.__family_name = family_name


	def getFamily_name(self) -> str:
		return self.__family_name


	def setName(self, name:str):
		self.__name = name


	def getName(self) -> str:
		return self.__name


	def setPatronymic(self, patronymic:str):
		self.__patronymic = patronymic


	def getPatronymic(self) -> str:
		return self.__patronymic


	def setGroup(self, group:str):
		self.__group = group


	def getGroup(self) -> str:
		return self.__group


	def delRating(self, subject:str):
		del self.__rating[subject]


	def changeRating(self, subject:str, rating:int):
		self.__rating[subject] = rating


	def getRating(self) -> dict:
		return self.__rating


	def PrintStudent(self, item:int):
		print(f'''
=== {item} ===
Фамилия: {self.__family_name}
Имя: {self.__name}
Отчество: {self.__patronymic}
Группа: {self.__group}
Оценки:''')

		if self.__rating:
			for i, elem in self.__rating.items():
				print(f'{i}: {elem}')

		else:
			print('    Нет оценок\n')


	def PrintStudentStr(self, item:int):
		print(f'{item}. {self.__family_name} {self.__name} {self.__patronymic}({self.__group})')
