import sys
import math
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from calc_ui import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.__result = None

		self.one.clicked.connect(self.clickButton)
		self.two.clicked.connect(self.clickButton)
		self.three.clicked.connect(self.clickButton)
		self.four.clicked.connect(self.clickButton)
		self.five.clicked.connect(self.clickButton)
		self.six.clicked.connect(self.clickButton)
		self.seven.clicked.connect(self.clickButton)
		self.eight.clicked.connect(self.clickButton)
		self.nine.clicked.connect(self.clickButton)
		self.zero.clicked.connect(self.clickButton)

		self.plus.clicked.connect(self.actionButton)
		self.minus.clicked.connect(self.actionButton)
		self.degree.clicked.connect(self.actionButton)
		self.multiplication.clicked.connect(self.actionButton)


	def clickButton(self):
		button = self.sender()

		if self.consol.text() == '0':
			self.consol.setText(button.text())

		else:
			if self.__result == self.consol.text():
				self.consol.setText(button.text())

			else:
				self.consol.setText(self.consol.text() + button.text())

		self.__result = 0


	def actionButton(self):
		button = self.sender()

		if self.consol.text()[-1] not in ['+', '-', '/', '*']:
			self.consol.setText(self.consol.text() + button.text())




if __name__ == "__main__":
	app = QApplication(sys.argv)

	a = Calculator()
	a.show()

	sys.exit(app.exec_())
