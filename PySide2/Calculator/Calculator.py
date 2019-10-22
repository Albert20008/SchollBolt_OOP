from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from State import State
from calc_ui import Ui_MainWindow


class Calculator(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()

		self.setupUi(self)

		self.__state = []

		self.__itemState = 0

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

		self.plus.clicked.connect(self.clickButton)
		self.minus.clicked.connect(self.clickButton)
		self.degree.clicked.connect(self.clickButton)
		self.multiplication.clicked.connect(self.clickButton)

		self.equally.clicked.connect(self.clickButton)

		self.clear.clicked.connect(self.discard)


	def clickButton(self):
		button = self.sender()

		self.__state[self.__itemState].clickButton(button)


	def discard(self):
		self.consol.setText('0')
		self.consol2.setText('0')
		self.__itemState = 0


	def setState(self, state:State):
		self.__state.append(state)


	def setItemState(self, item:int):
		self.__itemState = item
