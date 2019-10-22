from ListObserver.ListObserver import listObserver
from ListObserver.Observer import Observer

a = listObserver()

a.setObserver(Observer())

a.append(7)

a.append(3)

a + [3]

a.append(4)

a.append(2)

for i in range(len(a)):
	if a[i] % 2 != 0:
		a.append(a[i] * 2)

print(a)
