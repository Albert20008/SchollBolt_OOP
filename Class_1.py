class Time:
	def __init__(self, hours=0, minutes=0, seconds=0):
		self.__hours = hours
		self.__minutes = minutes
		self.__seconds = seconds


	def getHours(self) -> int:
		return self.__hours


	def setHours(self, hours:int):
		if 0 <= hours < 24:
			self.__hours = hours

		else:
			raise Exception('Неверное значение часа')


	def getMinutes(self) -> int:
		return self.__minutes


	def setMinutes(self, minutes:int):
		if 0 <= minutes < 60:
			self.__minutes = minutes

		else:
			raise Exception('Неверное значение минут')


	def getSeconds(self) -> int:
		return self.__seconds


	def setSeconds(self, seconds:int):
		if 0 <= seconds < 60:
			self.__seconds = seconds

		else:
			raise Exception('Неверное значение секунд')

	def onDayChange(self, d):
		pass


	def shiftTime(self, shift:int):
		self.__seconds += shift

		self.__minutes += self.__seconds // 60

		self.__seconds %= 60

		hours = self.__hours + self.__minutes // 60

		self.__hours = hours % 24

		self.__minutes %= 60

		self.onDayChange(hours // 24)

class Data(Time):
	def __init__(self, days=1, months=1, years=1):
		self.__days = days
		self.__months = months
		self.__years = years

	def onDayChange(self, d:int):
		self.shiftData(d)


	def days_in_months(self):
		if ((self.__years % 4 == 0) and (self.__years % 100 != 0)) or (self.__years % 400 == 0):
			return [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

		else:
			return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


	def getDays(self) -> int:
		return self.__days


	def setDays(self, days:int):
		if 0 < days < 32:

			if self.__months in [4, 6, 9, 11] and days == 31:

				raise Exception('Неверное значение дня')

			elif self.__months == 2 and days > 28:

				if days > 29:

					raise Exception('Неверное значение дня')

				elif not (((self.__years % 4 == 0) and (self.__years % 100 != 0)) or (self.__years % 400 == 0)):

					raise Exception('Неверное значение дня')

			self.__days = days

		else:
			raise Exception('Неверное значение дня')


	def getMonths(self) -> int:
		return self.__months

	def setMonths(self, months:int):
		if 0 < months < 13:

			self.__months = months

		else:
			raise Exception('Неверное значение месяца')

	def getYears(self) -> int:
		return self.__years

	def setYears(self, years:int):
		if years != 0:

			self.__years = years

		else:
			raise Exception('Неверное значение года')

	def shiftData(self, shift:int):
		day_months = self.days_in_months()

		if shift >= 0:
			self.__days += shift

			while self.__days > day_months[self.__months - 1]:
				self.__days -= day_months[self.__months - 1]
				self.__months += 1

				if self.__months == 13:
					self.__years += 1
					self.__months = 1

					if self.__years == 0:
						self.__years = 1

					day_months = self.days_in_months()

		else:
			self.__days += shift

			while self.__days <= 0:
				self.__months = self.__months - 1 if self.__months - 1 > 0 else 12
				self.__days += day_months[self.__months - 1]

				if self.__months == 12:
					self.__years -= 1

					if self.__years == 0:
						self.__years = -1

					day_months = self.days_in_months()


main = Data()

hours = int(input('Введите часы: '))
try:
	main.setHours(hours)
except Exception as e:
	raise e

minutes = int(input('Введите минуты: '))
try:
	main.setMinutes(minutes)
except Exception as e:
	raise e

seconds = int(input('Введите секунды: '))
try:
	main.setSeconds(seconds)
except Exception as e:
	raise e

years = int(input('Введите год: '))
try:
	main.setYears(years)
except Exception as e:
	raise e

months = int(input('Введите месяц: '))
try:
	main.setMonths(months)
except Exception as e:
	raise e

days = int(input('Введите день: '))
try:
	main.setDays(days)
except Exception as e:
	raise e

print('{} часов\n{} минут\n{} секунд'.format(main.getHours(), main.getMinutes(), main.getSeconds()))

years = main.getYears()
if years > 0:
	print('{} кол-во годов'.format(years))

else:
	print('{} кол-во годов до нашей эры'.format(years * -1))

print('{} номер месяца\n{} день'.format(main.getMonths(), main.getDays()))

shift = int(input('Насколько секунд изменить время?: '))

main.shiftTime(shift)

print('{} часов\n{} минут\n{} секунд'.format(main.getHours(), main.getMinutes(), main.getSeconds()))

years = main.getYears()
if years > 0:
	print('{} кол-во годов'.format(years))

else:
	print('{} кол-во годов до нашей эры'.format(years * -1))

print('{} номер месяца\n{} день'.format(main.getMonths(), main.getDays()))

shift = int(input('Насколько дней изменить дату?: '))

main.shiftData(shift)

print('{} часов\n{} минут\n{} секунд'.format(main.getHours(), main.getMinutes(), main.getSeconds()))

years = main.getYears()
if years > 0:
	print('{} кол-во годов'.format(years))

else:
	print('{} кол-во годов до нашей эры'.format(years * -1))

print('{} номер месяца\n{} день'.format(main.getMonths(), main.getDays()))

years = main.getYears()

if years > 0:
	print('{} кол-во годов'.format(years))

else:
	print('{} кол-во годов до нашей эры'.format(years * -1))


print('{} номер месяца\n{} кол-во дней'.format(main.getMonths(), main.getDays()))
