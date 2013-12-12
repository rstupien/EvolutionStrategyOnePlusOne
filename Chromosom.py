"""
Klasa przechowuje chromosom skladajacy sie z dwoch genow typu double. Udostepnia medtody pozwalajace pobierac wartosci genow
"""
class Chromosom(object):

	"""
	Konstruktor przypisujacy chromosomowi zadane wartosci
	"""
	def __init__(self, genX1, genX2):
		self.genX1 = genX1
		self.genX2 = genX2

	"""
	Oblicza funkcje przystosowania dla funkcji celu na podstawie chromosomu
	"""
	@property
	def obliczPrzystosowanie(self):
		return -1 * ((self.genX1 + 2*self.genX2 - 7)*(self.genX1 + 2*self.genX2 - 7) + (2*self.genX1 + self.genX2 -5 )*(2*self.genX1 + self.genX2 -5 ))
