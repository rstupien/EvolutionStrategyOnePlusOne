from Chromosom import *
from StrategiaEwolucyjna import *
from pylab import *

sigma = 1.0
K = 4
C1 = 0.9
C2 = 1.0 / C1
historiaSukcesow = []

genx = []
geny = []
genz = []

#nasze zmienne
x = 4
y = 4
xMin = -5
xMax = 5
yMin = -5
yMax = 5
liczbaIteracji = 926

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
	genx.append(chromosomRodzic.genX1)
	geny.append(chromosomRodzic.genX2)
	genz.append(np.sqrt(((chromosomRodzic.genX1 + 2*chromosomRodzic.genX2 - 7)*(chromosomRodzic.genX1 + 2*chromosomRodzic.genX2 - 7) + (2*chromosomRodzic.genX1 + chromosomRodzic.genX2 -5 )*(2*chromosomRodzic.genX1 + chromosomRodzic.genX2 -5 ))))

from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.gca(projection='3d')
X = np.arange(-6, 6, .4)
Y = np.arange(-6, 6, .4)
X, Y = np.meshgrid(X, Y)
Z = np.sqrt( ((X + 2*Y - 7)*(X + 2*Y - 7) + (2*X + Y -5 )*(2*X + Y -5 )))
#surf = ax.plot_surface(X, Y, R, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0, antialiased=False)

ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

ax.set_zlim(0, 15)

ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
ax.scatter(genx, geny, genz)

plt.show()

# co ma byc na wykresach? -- funkcja + kroki, jeden dla poprawnych + jeden dla wszystkich, na wykresie funkcji celu nasza sciezka (na praboli)
# dziecko ( liczbyiteracji), + wykres fazowy x1 i x2
