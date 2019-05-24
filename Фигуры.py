from abc import ABC, abstractmethod
from math import sqrt

class Figures(ABC):

	@abstractmethod
	def shooting(self, x, y):
		pass


class Circle(Figures):
	def __init__(self, r, x, y):
		self.r = r
		self.x = x
		self.y = y

	def shooting(self, x, y):

		if sqrt((self.x - x) * (self.x - x) + (self.y - y) * (self.y - y)) <= self.r:
			print('Попал\n*звук собаки, которая несёт утку*')

		else:
			print('Непопал\n*звук хохочущий над тобой собаки*')


class Square(Figures):
	def __init__(self, a, x, y):
		self.a = a
		self.x = x
		self.y = y


	def shooting(self, x, y):
		
		if self.x <= x <= self.x + self.a and self.y <= y <= self.y + self.a:
			print('Попал\n*звук собаки, которая несёт утку*')

		else:
			print('Непопал\n*звук хохочущий над тобой собаки*')


check = False
while not check:
	main = input('1: Круг\n2: Квадрат\nВыберите фигуру(запишите название или номер фигуры): ')

	if main in ['1', 'Круг', 'круг']:
		
		r = int(input('Введите радиус окружности: '))

		x = int(input('Введите координату x: '))

		y = int(input('Введите координату y: '))

		main = Circle(r, x, y)

		x = int(input('Введите координату x вашего выстрела: '))

		y = int(input('Введите координату y вашего выстрела: '))

		main.shooting(x, y)

		check = True

	elif main in ['2', 'Квадрат', 'квадрат']:

		a = int(input('Введите длинну стороны квадрата: '))

		x = int(input('Введите координату x: '))

		y = int(input('Введите координату y: '))

		main = Square(a, x, y)

		x = int(input('Введите координату x вашего выстрела: '))

		y = int(input('Введите координату y вашего выстрела: '))

		main.shooting(x, y)

		check = True

	else:
		print('Неверно!!!')

