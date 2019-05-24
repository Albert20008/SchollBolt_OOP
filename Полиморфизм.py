from abc import ABC, abstractmethod


class Animal(ABC):
	@abstractmethod
	def says(self):
		pass

class Cat(Animal):
	def says(self):
		print('Meow')

class Dog(Animal):
	def says(self):
		print('Wow')

Neko = Cat()
Neko.says()

dog = Dog()
dog.says()
