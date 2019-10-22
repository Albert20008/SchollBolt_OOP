from State import State


class State4(State):
	def __init__(self, descendant):
		self.__descendant = descendant


	def clickButton(self, button):
		letters = button.text()

		descendant = self.__descendant

		if letters is '=':
			expression = descendant.consol.text() + descendant.consol2.text()

			x = ''
			listExpression = []

			for i in range(len(expression)):
				if expression[i] in ['+', '-', '*', '/']:
					listExpression.append(int(x))
					listExpression.append(expression[i])
					x = ''

				else:
					x += expression[i]
			listExpression.append(int(x))

			answer = listExpression[0]

			for i in range(1, len(listExpression), 2):
				if listExpression[i] is '+':
					answer += listExpression[i + 1]

				elif listExpression[i] is '-':
					answer -= listExpression[i + 1]

				elif listExpression[i] is '*':
					answer *= listExpression[i + 1]

				elif listExpression[i] is '/':
					answer //= listExpression[i + 1]

			descendant.consol.setText('0')
			descendant.consol2.setText(str(answer))

		elif letters in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
			descendant.consol2.setText(letters)
			descendant.setItemState(0)

		elif letters in ['+', '-', '*', '/']:
			descendant.setItemState(1)
			descendant.clickButton()
