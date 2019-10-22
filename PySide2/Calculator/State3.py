from State import State


class State3(State):
	def __init__(self, descendant):
		self.__descendant = descendant


	def clickButton(self, button):
		letters = button.text()

		descendant = self.__descendant

		if letters in ['+', '-', '*', '/']:
			descendant.setItemState(1)
			descendant.clickButton()

		elif letters in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
			descendant.consol2.setText(descendant.consol2.text() + letters)

		elif letters is '=':
			descendant.setItemState(3)
			descendant.clickButton()
