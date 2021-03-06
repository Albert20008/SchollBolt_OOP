class Singleton(type):
	instances = {}

	def __call__(cls, *args, **NameArgs):
		if cls not in cls.instances:
			cls.instances[cls] = super(Singleton, cls).__call__(*args, **NameArgs)

		return cls.instances[cls] 
