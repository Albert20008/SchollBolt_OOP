import sys
import math
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Calculator(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('Регистрация студента')

		menuBox = QVBoxLayout()

		string = QLabel('ИНФОРМАЦИЯ О СТУДЕНТЕ')
		menuBox.addWidget(string)

		family_name = QLabel('Фамилия: ')
		consolFamily_name = QLineEdit()

		name = QLabel('Имя: ')
		consolName = QLineEdit()

		patronymic = QLabel('Отчество: ')
		consolPatronymic = QLineEdit()

		stading = QLabel('Учится: ')
		buttonStading = QCheckBox()

		menu = QFormLayout()

		menu.addRow(family_name, consolFamily_name)
		menu.addRow(name, consolName)
		menu.addRow(patronymic, consolPatronymic)
		menu.addRow(stading, buttonStading)
		menuBox.addLayout(menu)

		buttons = QHBoxLayout()

		buttons.addStretch()

		buttonOK = QPushButton('OK')
		buttons.addWidget(buttonOK)

		buttonClose = QPushButton('Отмена')
		buttons.addWidget(buttonClose)

		menuBox.addLayout(buttons)

		self.setLayout(menuBox)

if __name__ == "__main__":
	a = QApplication(sys.argv)
	w = Calculator()
	w.show()
	sys.exit(a.exec_())
