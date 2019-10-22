from Object.Case import Case
from Object.File import File
from Object.System import System
from Object.Caretaker import Caretaker


CareTaker = Caretaker()

system = System()

system.add(File('Документ', 'А ШО ЭТО ВЫ ДЕЛАЕТЕ В МОЁМ ХОЛОДИЛЬНИКЕ?:*'))
system.add(File('Тут ничего нет', 'Ну я же говорил тут пусто'))

system.add(Case(name='Папка_1'))

system.getOneElement(2).add(File('Документ_1', '12345'))

CareTaker.pushState(system.createMemento())

print('Тут просто файлики')

system.run()

system.add(File('Штука, которая несохранится'))

print('Здесь должна быть штука, которая несохранится')

system.run()

system.restore(CareTaker.popState())

print('А вот тут мы восстановили систему, и штуки тут нет')

system.run()
