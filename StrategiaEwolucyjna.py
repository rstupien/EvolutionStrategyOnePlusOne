from Chromosom import *
import random

def mutuj(chromosomMutowany, sigma):
	return Chromosom(chromosomMutowany.genX1 + sigma * random.normalvariate(0.0, 1.0), chromosomMutowany.genX2 + sigma * random.normalvariate(0.0, 1.0))

def sprawdzCzyDzieckoLepsze(chromosomDziecko, chromosomRodzic):
	if (chromosomDziecko.obliczPrzystosowanie > chromosomRodzic.obliczPrzystosowanie):
		return 1
	else:
		return 0

def aktualizujHistorieSukcesow(czyDzieckoLepsze, historiaSukcesow):
	for i in reversed(range(0,len(historiaSukcesow))):
		historiaSukcesow[i] = historiaSukcesow[i-1]

	historiaSukcesow[0] = czyDzieckoLepsze
	return historiaSukcesow

def zmienSigme(sigma, historiaSukcesow, C1, C2):
	jednaPiata = 0.2
	licznik = 0.0
	
	for i in range(len(historiaSukcesow)):
		licznik += historiaSukcesow[i]
	
	stosunekSukcesowDoPorazek = licznik / len(historiaSukcesow)

	if (stosunekSukcesowDoPorazek > jednaPiata):
		return C2 * sigma

	if (stosunekSukcesowDoPorazek < jednaPiata):
		return C1 * sigma
