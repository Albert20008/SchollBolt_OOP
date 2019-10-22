import sys
import math
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from calc_ui import Ui_MainWindow

class Calculator(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.one.clicked.connect(self.handleDigit)

	def handleDigit(self):
		print("asasds")
