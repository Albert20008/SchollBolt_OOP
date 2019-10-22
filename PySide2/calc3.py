import sys
import math
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class SimpleCalculator(QWidget):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("Простой калькулятор")

		le1 = QLineEdit()
		le2 = QLineEdit()
		plus = QLabel("+")
		equals = QPushButton("=")
		result = QLabel("")

		layout = QHBoxLayout()
		layout.addWidget(le1)
		layout.addWidget(plus)
		layout.addWidget(le2)
		layout.addWidget(equals)
		layout.addWidget(result)

		self.setLayout(layout)

		self.le1 = le1
		self.le2 = le2
		self.result = result
		equals.clicked.connect(self.calculate)

	def calculate(self):
		try:
			val1 = float(self.le1.text())
		except:
			val1 = 0

		try:
			val2 = float(self.le2.text())
		except:
			val2 = 0

		r = val1 + val2

		self.result.setText(str(r))


if __name__ == "__main__":
	a = QApplication(sys.argv)
	w = SimpleCalculator()
	w.show()
	sys.exit(a.exec_())
