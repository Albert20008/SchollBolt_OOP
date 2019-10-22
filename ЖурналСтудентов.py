from classes.SimpleMenuItem import SimpleMenuItem
from classes.Menu import Menu
from classes.Student import Student
from classes.StudentReg import StudentReg
from classes.Chosen import Chosen
from classes.StudentVisitor import BriefPrintVisitor



def function():
	print('''
Для доступа к этой функции вам необходима платная версия программы
Для того чтобы получить платную версию необходимо перевести на Qiwi-кошелёк под номером 89821046254 1000 рублей
Если вы перевели указанную сумму, но доступ до сих пор не открыт, повторите операцию с переводом денег:)
''')


def _print(arg):
	pass



def Start():
	lenRegister = functions.LenRegister()

	if lenRegister:
		functions.visit(BriefPrintVisitor())

		chosen = Chosen()
		chosen.item = int(input('Введите номер студента: ')) - 1

	else:
		print('Студентов нет')


def Print():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		functions.getStudent(item).PrintStudent(item + 1)


def End():
	chosen = Chosen()

	chosen.item = None


def change_family_name():
	chosen = Chosen()
	item = chosen.item
	
	if item != None:
		family_name = input('Введите новую фамилию: ')

		apostate = functions.getStudent(item)

		apostate.setFamily_name(family_name)
		functions.save()

	else:
		print('Студентов нет')

def change_name():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		name = input('Введите новое имя: ')

		apostate = functions.getStudent(item)

		apostate.setName(name)
		functions.save()

	else:
		print('Студентов нет')


def change_patronymic():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		patronymic = input('Введите новое отчество: ')

		apostate = functions.getStudent(item)

		apostate.setPatronymic(patronymic)
		functions.save()

	else:
		print('Студентов нет')



def change_group():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		group = input('Введите новую группу: ')

		apostate = functions.getStudent(item)

		apostate.setGroup(group)
		functions.save()


	else:
		print('Студентов нет')


def add_value():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		apostate = functions.getStudent(item)
	        
		keys = input('Введите предмет: ')

		while keys in apostate.getRating():
			print('Ошибка!!!\nВведите не существующий в программе предмет')

			keys = input('Введите предмет: ')

		check = False

		while not check:
			try:
				value = int(input('Введите оценку: '))
			except ValueError as e:
				print('Введите число!!!')

			else:
				if value > 0:
					check = True

				else:
					print('Введите число больше нуля')

		apostate.changeRating(keys, value)
		functions.save()


	else:
		print('Студентов нет')	


def change_value():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		apostate = functions.getStudent(item)

		if apostate.getRating():
			keys = input('Введите предмет: ')

			while keys not in apostate.getRating():
				print('Ошибка\nВведите существующий предмет')

				keys = input('Введите предмет: ')

			check = False

			while not check:
				try:
					value = int(input('Введите новую оценку: '))
				except ValueError as e:
					print('Введите число!!!')
				else:
					if value >= 0:
						check = True

					else:
						print('Введите число больше нуля!!!')

			apostate.changeRating(keys, value)
			functions.save()


		else:
			print('Оценок нет!')

	else:
		print('Студентов нет')	


def del_value():
	chosen = Chosen()
	item = chosen.item

	if item != None:
		apostate = functions.getStudent(item)

		if apostate.getRating():

			keys = input('Введите предмет: ')

			check = input('Вы уверены?(да/нет): ')

			while check not in ['Нет', 'нет', 'НЕТ']:
					if check in ['Да', 'да', 'ДА']:
						apostate.delRating(keys)
						functions.save()
						break

					else:
						print('Ошибка\nВведите да или нет!')

						check = input('Вы уверены?(да/нет): ')

		else:
			print('Оценок нет!')

	else:
		print('Студентов нет')	


def add_student():
	family_name = input('Введите фамилию: ')

	name = input('Введите имя: ')

	patronymic = input('Введите отчество: ')

	group = input('Введите группу: ')

	functions.add_student(family_name, name, patronymic, group)


def del_student():
	register = functions.getRegister()

	if register:
		functions.visit(BriefPrintVisitor())

		item = int(input('Введите номер студента: '))

		while item < 1 or item > len(register):
			print('Студента с таким номером нет\nПовторите попытку')
			item = int(input('Введите номер студента: '))

		check = input('Вы уверены?: ')

		while check not in ['Нет', 'нет', 'НЕТ']:
			if check in ['Да', 'да', 'ДА']:
				functions.del_student(item - 1)
				break

			else:
				print('Ошибка\nВведите да или нет!')
				check = input('Вы уверены?: ')

	else:
		print('Нет студентов')


functions = StudentReg()

menu = Menu('',  [
SimpleMenuItem('Список студентом', functions.list_student),
SimpleMenuItem('Добавить студента', add_student)],
)

Submenu = menu.AddSubmenu('Редактировать студента', [
SimpleMenuItem('Изменить фамилию', change_family_name),
SimpleMenuItem('Изменить имя', change_name),
SimpleMenuItem('Изменить отчество', change_patronymic),
SimpleMenuItem('Изменить группу', change_group)]
)

Submenu.AddSubmenu('Изменить оценки', [
SimpleMenuItem('Добавить оценку', add_value),
SimpleMenuItem('Изменить оценку', change_value),
SimpleMenuItem('Удалить оценку', del_value)]
)

Submenu.SetStartAction(Start)
Submenu.SetEndAction(End)
Submenu.SetPrintAction(Print)

menu.add('Удалить студента', del_student)
menu.add('Вывести отличников', functions.good_student)
menu.add('Вывести неуспевающих', functions.low_student)

menu.run()
