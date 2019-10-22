import sys
import math
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from Calculator import Calculator
from State1 import State1
from State2 import State2
from State3 import State3
from State4 import State4
from calc_ui import Ui_MainWindow

if __name__ == "__main__":
	app = QApplication(sys.argv)

	a = Calculator()

	a.setState(State1(a))
	a.setState(State2(a))
	a.setState(State3(a))
	a.setState(State4(a))

	a.show()

	sys.exit(app.exec_())
