from Chromosom import *
from StrategiaEwolucyjna import *
from pylab import *
import Tkinter

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
liczbaIteracji = 100

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

        xMinLabel = Tkinter.Label(self, text="xMin")
        xMinLabel.grid(column=0,row=2)
        self.xMinValue = Tkinter.StringVar()
        self.xMinEntry = Tkinter.Entry(self,textvariable=self.xMinValue)
        self.xMinEntry.grid(column=0,row=3,sticky='EW')
        self.xMinValue.set(xMin)
        
        xMaxLabel = Tkinter.Label(self, text="xMax")
        xMaxLabel.grid(column=1,row=2)
        self.xMaxValue = Tkinter.StringVar()
        self.xMaxEntry = Tkinter.Entry(self,textvariable=self.xMaxValue)
        self.xMaxEntry.grid(column=1,row=3,sticky='EW')
        self.xMaxValue.set(xMax)

        xLabel = Tkinter.Label(self, text="x")
        xLabel.grid(column=2,row=2)
        self.xValue = Tkinter.StringVar()
        self.xEntry = Tkinter.Entry(self,textvariable=self.xValue)
        self.xEntry.grid(column=2,row=3,sticky='EW')
        self.xValue.set(x)

        yMinLabel = Tkinter.Label(self, text="yMin")
        yMinLabel.grid(column=0,row=4)
        self.yMinValue = Tkinter.StringVar()
        self.yMinEntry = Tkinter.Entry(self,textvariable=self.yMinValue)
        self.yMinEntry.grid(column=0,row=5,sticky='EW')
        self.yMinValue.set(yMin)

        yMaxLabel = Tkinter.Label(self, text="yMax")
        yMaxLabel.grid(column=1,row=4)
        self.yMaxValue = Tkinter.StringVar()
        self.yMaxEntry = Tkinter.Entry(self,textvariable=self.yMaxValue)
        self.yMaxEntry.grid(column=1,row=5,sticky='EW')
        self.yMaxValue.set(yMax)

        yLabel = Tkinter.Label(self, text="y")
        yLabel.grid(column=2,row=4)
        self.yValue = Tkinter.StringVar()
        self.yEntry = Tkinter.Entry(self,textvariable=self.yValue)
        self.yEntry.grid(column=2,row=5,sticky='EW')
        self.yValue.set(y)

        liczbaIteracjiLabel = Tkinter.Label(self, text="liczbaIteracji")
        liczbaIteracjiLabel.grid(column=0,row=6)
        self.liczbaIteracjiValue = Tkinter.StringVar()
        self.liczbaIteracjiEntry = Tkinter.Entry(self,textvariable=self.liczbaIteracjiValue)
        self.liczbaIteracjiEntry.grid(column=0,row=7,sticky='EW')
        self.liczbaIteracjiValue.set(liczbaIteracji)


        startButton = Tkinter.Button(self,text=u"Start", command=self.startButtonClick)
        startButton.grid(column=1,row=8)

        Wykres1Button = Tkinter.Button(self,text=u"Wykres 1", command=self.wykres1ButtonClick)
        Wykres1Button.grid(column=0,row=9)

        Wykres2Button = Tkinter.Button(self,text=u"Wykres 2")
        Wykres2Button.grid(column=1,row=9)

        Wykres3Button = Tkinter.Button(self,text=u"Wykres 3")
        Wykres3Button.grid(column=2,row=9)

        Wykres4Button = Tkinter.Button(self,text=u"Wykres 4")
        Wykres4Button.grid(column=0,row=10)

        self.resizable(False,False)

    def startButtonClick(self):
        global C1
        global C2
        global K
        global xMin
        global xMax
        global x
        global yMin
        global yMax
        global y
        global liczbaIteracji
        global sigma
        global historiaSukcesow
        global genx
        global geny
        global genz

        C1 = float(self.C1Value.get())
        C2 = float(self.C2Value.get())
        K = int(self.KValue.get())
        xMin = float(self.xMinValue.get())
        xMax = float(self.xMaxValue.get())
        x = float(self.xValue.get())
        yMin = float(self.yMinValue.get())
        yMax = float(self.yMaxValue.get())
        y = float(self.yValue.get())
        liczbaIteracji = int(self.liczbaIteracjiValue.get())

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
            x = chromosomRodzic.genX1
            y = chromosomRodzic.genX2
            genx.append(x)
            geny.append(y)
            genz.append(np.sqrt(((x + 2*y - 7)*(x + 2*y - 7) + (2*x+ y -5 )*(2*x + y -5 ))))

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

        line_ani = animation.FuncAnimation(fig, update_lines, 100,
                                           interval = 150, blit=False)
        plt.show()

app = appGUIp(None)
app.title('PSZT')
app.mainloop()

# co ma byc na wykresach? -- funkcja + kroki, jeden dla poprawnych + jeden dla wszystkich, na wykresie funkcji celu nasza sciezka (na praboli)
# dziecko ( liczbyiteracji), + wykres fazowy x1 i x2