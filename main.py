# -*- coding: utf-8 -*-

from Chromosom import *
from StrategiaEwolucyjna import *
from pylab import *
import Tkinter
import tkMessageBox

"""
Stale
"""
sigma = 1.0
K = 4
C1 = 0.9
C2 = 1.0 / C1
historiaSukcesow = []

"""
Tablice przygotowane na dane do wykresow
"""
genxxAll = []
genyyAll = []
genzzAll = []
genx = []
geny = []
genz = []

"""
Zmienne, poczatkowo zainisjalizowane
"""
x = 4
y = 4
xMin = -5
xMax = 5
yMin = -5
yMax = 5
liczbaIteracji = 1000

"""
GUI
"""
class appGUIp(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()

    def initialize(self):
        self.grid()
        
        C1Label = Tkinter.Label(self, text="C1")
        C1Label.grid(column=0,row=0)
        self.C1Value = Tkinter.StringVar()
        self.C1Entry = Tkinter.Entry(self,textvariable=self.C1Value)
        self.C1Entry.grid(column=0,row=1,sticky='EW')
        self.C1Value.set(C1)

        C2Label = Tkinter.Label(self, text="C2")
        C2Label.grid(column=1,row=0)
        self.C2Value = Tkinter.StringVar()
        self.C2Entry = Tkinter.Entry(self,textvariable=self.C2Value)
        self.C2Entry.grid(column=1,row=1,sticky='EW')
        self.C2Value.set(C2)    

        KLabel = Tkinter.Label(self, text="K")
        KLabel.grid(column=2,row=0)
        self.KValue = Tkinter.StringVar()
        self.KEntry = Tkinter.Entry(self,textvariable=self.KValue)
        self.KEntry.grid(column=2,row=1,sticky='EW')
        self.KValue.set(K)

        xLabel = Tkinter.Label(self, text="x")
        xLabel.grid(column=0,row=2)
        self.xValue = Tkinter.StringVar()
        self.xEntry = Tkinter.Entry(self,textvariable=self.xValue)
        self.xEntry.grid(column=0,row=3,sticky='EW')
        self.xValue.set(x)

        yLabel = Tkinter.Label(self, text="y")
        yLabel.grid(column=1,row=2)
        self.yValue = Tkinter.StringVar()
        self.yEntry = Tkinter.Entry(self,textvariable=self.yValue)
        self.yEntry.grid(column=1,row=3,sticky='EW')
        self.yValue.set(y)

        liczbaIteracjiLabel = Tkinter.Label(self, text="liczbaIteracji")
        liczbaIteracjiLabel.grid(column=2,row=2)
        self.liczbaIteracjiValue = Tkinter.StringVar()
        self.liczbaIteracjiEntry = Tkinter.Entry(self,textvariable=self.liczbaIteracjiValue)
        self.liczbaIteracjiEntry.grid(column=2,row=3,sticky='EW')
        self.liczbaIteracjiValue.set(liczbaIteracji)


        startButton = Tkinter.Button(self,text=u"Start", command=self.startButtonClick)
        startButton.grid(column=0,row=4)

        Wykres1Button = Tkinter.Button(self,text=u"Wykres 1", command=self.wykres1ButtonClick)
        Wykres1Button.grid(column=1,row=4)

        Wykres2Button = Tkinter.Button(self,text=u"Wykres 2", command=self.wykres2ButtonClick)
        Wykres2Button.grid(column=2,row=4)

        self.resizable(False,False)

	"""
	Przycisk start
	"""
    def startButtonClick(self):
        global C1
        global C2
        global K
        global x
        global y
        global liczbaIteracji
        global sigma
        global historiaSukcesow
        global genx
        global geny
        global genz
        global genxxAll
        global genyyAll
        global genzzAll

	"""
	Pobranie wartosci z pol w GUI
	"""
        C1 = float(self.C1Value.get())
        C2 = float(self.C2Value.get())
        K = int(self.KValue.get())
        x = float(self.xValue.get())
        y = float(self.yValue.get())
        liczbaIteracji = int(self.liczbaIteracjiValue.get())
	"""
	Wyzerowanie tablic
	"""
        genx = []
        geny = []
        genz = []
        genxxAll = []
        genyyAll = []
        genzzAll = []

	"""
	Utworzenie nowego rodzica
	"""
        chromosomRodzic = Chromosom(x,y)
        for i in range(K):
            historiaSukcesow.append(0)

	"""
	Glowna petla programu
	"""
        for i in range(liczbaIteracji):
            chromosomDziecko = mutuj(chromosomRodzic, sigma)

#Zebranie danych wszystkich (i gorszych i lepszych dzieci/rodzicow)
            xx = chromosomDziecko.genX1
            yy = chromosomDziecko.genX2
            genxxAll.append(xx)
            genyyAll.append(yy)
            genzzAll.append(np.sqrt(((xx + 2*yy - 7)*(xx + 2*yy - 7) + (2*xx+ yy -5 )*(2*xx + yy -5 ))))


#Sprawdzenie czy dziecko lepsze

            lepsze = sprawdzCzyDzieckoLepsze(chromosomDziecko, chromosomRodzic)
            if (lepsze == 1):
                chromosomRodzic = chromosomDziecko
            historiaSukcesow = aktualizujHistorieSukcesow(lepsze, historiaSukcesow)

#Zmiana sigmy

            if (i % K == 0):
                sigma = zmienSigme(sigma, historiaSukcesow, C1, C2)
            print chromosomRodzic.genX1, chromosomRodzic.genX2, sigma, xx, yy

#Zebranie danych do wykresu z lepiej przystosowanymi

            x = chromosomRodzic.genX1
            y = chromosomRodzic.genX2
            genx.append(x)
            geny.append(y)
            genz.append(np.sqrt(((x + 2*y - 7)*(x + 2*y - 7) + (2*x+ y -5 )*(2*x + y -5 ))))

        komunikat = u"X optymalne = "+str(x)+u"\nY optymalne = "+str(y)+u"\nWartość funkcji = "+str(genz[-1])
        tkMessageBox.showinfo(u"Wynik",komunikat)

	"""
	Wyrysowanie wykresu pierwzego, jedynie z lepszymi chromosomami (2D animacja i 3D)
	"""
    def wykres1ButtonClick(self):
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator, FormatStrFormatter
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        import numpy as np

        fig = plt.figure()
        ax = fig.add_subplot(1, 2, 1, projection = '3d')

        X = np.arange(-6, 6, .4)
        Y = np.arange(-6, 6, .4)
        X, Y = np.meshgrid(X, Y)
        Z = np.sqrt( ((X + 2*Y - 7)*(X + 2*Y - 7) + (2*X + Y -5 )*(2*X + Y -5 )))

        ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

        ax.set_zlim(0, 15)

        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        ax2 = fig.add_subplot(1,2,2)

        def update_lines(num):
            line = ax.scatter(genx[:num], geny[:num], genz[:num])
            line = ax2.plot(genz[:num])
            return line,

        line_ani = animation.FuncAnimation(fig, update_lines, liczbaIteracji,
                                           interval = 150, blit=False)
        plt.show()
	"""
	Wyrysowanie wykresu drugiego z wszystkimi danymi
	"""
    def wykres2ButtonClick(self):
        from mpl_toolkits.mplot3d import Axes3D
        from matplotlib import cm
        from matplotlib.ticker import LinearLocator, FormatStrFormatter
        import matplotlib.pyplot as plt
        import matplotlib.animation as animation
        import numpy as np

        fig = plt.figure()
        ax = fig.add_subplot(1, 2, 1, projection = '3d')

        X = np.arange(-6, 6, .4)
        Y = np.arange(-6, 6, .4)
        X, Y = np.meshgrid(X, Y)
        Z = np.sqrt( ((X + 2*Y - 7)*(X + 2*Y - 7) + (2*X + Y -5 )*(2*X + Y -5 )))

        ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)

        ax.set_zlim(0, 15)

        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
        ax2 = fig.add_subplot(1,2,2)

        def update_lines(num):
            line = ax.scatter(genxxAll[:num], genyyAll[:num], genzzAll[:num])
            line = ax2.plot(genzzAll[:num])
            return line,

        line_ani = animation.FuncAnimation(fig, update_lines, liczbaIteracji,
                                           interval = 150, blit=False)
        plt.show()



app = appGUIp(None)
app.title('Strategia ewolucyjna 1+1')
app.mainloop()
