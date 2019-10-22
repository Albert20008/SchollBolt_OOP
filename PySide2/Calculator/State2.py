from State import State


class State2(State):
	def __init__(self, descendant):
		self.__descendant = descendant


	def clickButton(self, button):
		letters = button.text()

		descendant = self.__descendant

		if letters in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
			descendant.consol2.setText(letters)
			descendant.setItemState(2)

		elif letters is '=':
			descendant.setItemState(3)
			descendant.clickButton()

		elif letters in ['+', '-', '*', '/']:
			if descendant.consol.text() is '0':
				descendant.consol.setText(descendant.consol2.text() + letters)

			else:
				descendant.consol.setText(descendant.consol.text() + descendant.consol2.text() + letters)
