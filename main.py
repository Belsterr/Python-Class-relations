class Car:
	def __init__(self, name):
		self.name = name
		self._engine = None
		self._manufacture = None
		
	@property
	def engines(self):
		return self._engine

	@engines.setter
	def engines(self, value):
		self._engine = value

	@property
	def manufacture(self):
		return self._manufacture

	@manufacture.setter
	def manufacture(self, value):
		self._manufacture = value

class Engine:
	def __init__(self, name):
		self.name = name


class Manufacturer:
	def __init__(self, name):
		self.name = name


fusca = Car('Fusca')
engin = Engine('2.1')
volks = Manufacturer('Volkswag')
fusca.engines = engin
fusca.manufacture = volks

print(f'Car: {fusca.name} \nEngine: {fusca.engines.name} \nManufacturer: {fusca.manufacture.name}')
print()

gol = Car('Gol')
volks = Manufacturer('Volkswag')
fusca.engines = engin
fusca.manufacture = volks

print(f'Car: {fusca.name} \nEngine: {fusca.engines.name} \nManufacturer: {fusca.manufacture.name}')
