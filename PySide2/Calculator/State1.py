from State import State


class State1(State):
	def __init__(self, descendant):
		self.__descendant = descendant


	def clickButton(self, button):
		letters = button.text()

		descendant = self.__descendant

		if letters in ['+', '-', '/', '*']:
			descendant.setItemState(1)
			descendant.clickButton()

		elif letters == '=':
			descendant.setItemState(3)
			descendant.clickButton()

		elif descendant.consol2.text() == '0':
			descendant.consol2.setText(button.text())

		else:
			descendant.consol2.setText(descendant.consol2.text() + button.text())
