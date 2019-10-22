from .StudentVisitor import StudentVisitor
from .Student import Student


class HighAchieverVisitor(StudentVisitor):
	def __init__(self, register:list):
		self.__register = register
		self.GoodStudent = False


	def startVisit(self):
		if self.__register:
			print('\nСтуденты-отличники:')


	def visitStudent(self, index:int, student:Student):
		check = True

		for g in student.getRating().values():

			if g < 5:
				check = False
				break

		if check:
			self.GoodStudent = True
			student.PrintStudentStr(index + 1)


	def finishVisit(self):
		if not self.GoodStudent:
			print('Отличников нет:(')
		print()


class LowAchieverVisitor(StudentVisitor):
	def __init__(self, register:list):
		self.__register = register
		self.LowStudent = False


	def startVisit(self):
		if self.__register:
			print('\nСтуденты-неуспевающие:')


	def visitStudent(self, index:int, student:Student):
		check = False

		for g in student.getRating().values():
			if g <= 2:
				check = True
				break


		if check:
			self.LowStudent = True
			student.PrintStudentStr(index + 1)


	def finishVisit(self):
		if not self.LowStudent:
			print('Неуспевающих нет:)')
		print()
