from Chromosom import *
from StrategiaEwolucyjna import *

sigma = 1.0
K = 4
C1 = 0.9
C2 = 1.0 / C1
historiaSukcesow = []

#nasze zmienne
x = 4
y = 4
xMin = -5
xMax = 5
yMin = -5
yMax = 5
liczbaIteracji = 695

chromosomRodzic = Chromosom(x,y)
for i in range(K):
	historiaSukcesow.append(0)

for i in range(liczbaIteracji):
	chromosomDziecko = mutuj(chromosomRodzic, sigma)
	lepsze = sprawdzCzyDzieckoLepsze(chromosomDziecko, chromosomRodzic)
	if (lepsze == 1):
		chromosomRodzic = chromosomDziecko
	historiaSukcesow = aktualizujHistorieSukcesow(lepsze, historiaSukcesow)
	if (i % K == 0):
		sigma = zmienSigme(sigma, historiaSukcesow, C1, C2)
	print chromosomRodzic.genX1, chromosomRodzic.genX2


# co ma byc na wykresach? -- funkcja + kroki, jeden dla poprawnych + jeden dla wszystkich, na wykresie funkcji celu nasza sciezka (na praboli)
# dziecko ( liczbyiteracji), + wykres fazowy x1 i x2
