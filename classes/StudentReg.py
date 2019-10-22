from struct import pack, unpack
from .Student import Student
from .Singleton import Singleton
from .StudentVisitor import StudentVisitor, DetailedPrintVisitor, BriefPrintVisitor
from .AchieverVisitor import HighAchieverVisitor, LowAchieverVisitor


# def Singleton(cls):
# 	instances = {}

# 	def getInstance(*args, **NameArgs):
# 		if cls not in instances:
# 			instances[cls] = cls(*args, **NameArgs)

# 		return instances[cls]

# 	return getInstance





#@Singleton
class StudentReg(metaclass=Singleton):
	def __init__(self):
		self.__register = self.load()


	def save(self):
		with open('Save/Save', 'wb') as file:
			file.write(pack('h', len(self.__register)))

			for i in range(len(self.__register)):

				family_name = self.__register[i].getFamily_name().encode('utf-8')
				lens = len(family_name)
				file.write(pack('h{}s'.format(lens), lens, family_name))

				name = self.__register[i].getName().encode('utf-8')
				lens = len(name)
				file.write(pack('h{}s'.format(lens), lens, name))

				patronymic = self.__register[i].getPatronymic().encode('utf-8')
				lens = len(patronymic)
				file.write(pack('h{}s'.format(lens), lens, patronymic))

				group = self.__register[i].getGroup().encode('utf-8')
				lens = len(group)
				file.write(pack('h{}s'.format(lens), lens, group))

				file.write(pack('h', len(self.__register[i].getRating())))

				for work, poin in self.__register[i].getRating().items():
					schoolwork = work.encode('utf-8')
					lens = len(schoolwork)
					file.write(pack('h{}sh'.format(lens), lens, schoolwork, poin))


	def load(self):

		data = []

		try:
			file = open('Save/Save', 'rb')
		except FileNotFoundError as e:
			pass

		else:
			lens = unpack('h', file.read(2))[0]

			for i in range(lens):

				lens = unpack('h', file.read(2))[0]
				family_name = unpack('{}s'.format(lens), file.read(lens))[0].decode('utf-8')

				lens = unpack('h', file.read(2))[0]
				name = unpack('{}s'.format(lens), file.read(lens))[0].decode('utf-8')

				lens = unpack('h', file.read(2))[0]
				patronymic = unpack('{}s'.format(lens), file.read(lens))[0].decode('utf-8')

				lens = unpack('h', file.read(2))[0]
				group = unpack('{}s'.format(lens), file.read(lens))[0].decode('utf-8')

				lens = unpack('h', file.read(2))[0]
				Rating = {}
				for g in range(lens):
					lens = unpack('h', file.read(2))[0]

					schoolwork = unpack('{}s'.format(lens), file.read(lens))[0].decode('utf-8')
					Rating[schoolwork] = unpack('h', file.read(2))[0]

				data.append(Student(family_name, name, patronymic, group, Rating))

			file.close()

		return data

	def list_student(self):
		self.visit(DetailedPrintVisitor(self.__register))


	def add_student(self, family_name:str, name:str, patronymic:str, group:str):
		self.__register.append(Student(family_name, name, patronymic, group))
		self.save()


	def del_student(self, item:int):
		del self.__register[item]
		self.save()


	def good_student(self):
		self.visit(HighAchieverVisitor(self.__register))


	def low_student(self):
		self.visit(LowAchieverVisitor(self.__register))


	def LenRegister(self) -> int:
		return len(self.__register)


	def getStudent(self, item:int):
		return self.__register[item]


	def getRegister(self):
		return self.__register


	def visit(self, visitor:StudentVisitor):
		visitor.startVisit()
		for i, student in enumerate(self.__register):
			visitor.visitStudent(i, student)
		visitor.finishVisit()
