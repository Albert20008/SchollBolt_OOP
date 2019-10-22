from abc import ABC, abstractmethod
from .Student import Student


class StudentVisitor(ABC):
	@abstractmethod
	def startVisit(self):
		pass


	@abstractmethod
	def visitStudent(self, index:int, student:Student):
		pass

	@abstractmethod
	def finishVisit(self):
		pass


class DetailedPrintVisitor(StudentVisitor):
	def __init__(self, register:list):
		self.__register = register


	def startVisit(self):
		if self.__register:
			print('Студенты:')


	def visitStudent(self, index:int, student:Student):
		student.PrintStudent(index + 1)


	def finishVisit(self):
		if not self.__register:
			print('Нет студентов')
		print()


class BriefPrintVisitor(StudentVisitor):
	def startVisit(self):
		pass


	def visitStudent(self, index:int, student:Student):
		student.PrintStudentStr(index + 1)


	def finishVisit(self):
		pass
