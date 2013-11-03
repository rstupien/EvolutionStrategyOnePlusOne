#ifndef STRATEGIA_EWOLUCYJNA_H
#define STRATEGIA_EWOLUCYJNA_H

#define K 4
#define C1 0.9
#define C2 1/C1

#include "Chromosom.h"
#include <random>

using namespace std;

class StrategiaEwolucyjna
{
    public:

    /**
    Konstruktor parametrowy.
    Przyjmuje zadana pare liczb jako punkt pracy algorytmu oraz przedzial na osi x1 oraz x2.
    */
    StrategiaEwolucyjna(double x10, double x20, double x1Min, double x1Max, double x2Min, double x2Max, int liczbaIteracji);

    ~StrategiaEwolucyjna();

    void start();

    private:

    /**
    Na podstawie poprzedniego rozwiazania, stalych, sigmy zwraca wzskaznik na zmutowany chromosom.
    */
    Chromosom* mutuj(Chromosom* mutowany);

    /**
    Sprawdza, czy zmutowany chromosom jest lepszy w sensie wartosci funkcji przystosowania i w zaleznosci od wyniku zostawia jako aktualny punkt rodzica albo dziecko.
    */
    bool sprawdzCzyZmutowanyJestLepszy (Chromosom* zmutowany);

    /**
    Na podstawie oceny jakosci ostatniej mutacji aktualizuje tablice historii sukcesow i porazek w sensie poprawy wartosci funkcji przystosowania.
    */
    void aktualizujHistorieSukcesow(bool czyZmutowanyJestLepszy);

    /**
    Na podstawie historii sukcesow modyfikuje parametr sigma.
    */
    void modyfikujSigme();





    /**
    Konstruktor bezparametrowy jest bez sensu i dlatego go zablokowano.
    */
    StrategiaEwolucyjna();

    /*---------------------------------------------------------------------*/

    /**
    Wskaznik na chromosom opisujacy obecne rozwiazanie.
    */
    Chromosom* rodzic;

    /**
    Parametr sigma sluzacy do polepszenia rozwiazania w algorytmie.
    */
    double sigma;

    /**
    Tablica zapisujaca w kolejnosci historycznej (najwczesniejszy indeks to 0, pozniejsze w kierunku  do K-1), czy w K poprzednich mutacjach poprawilismy wynik funkcji przystosowania, czy nie.
    Przyjmuje wartosci true/false.
    */
    bool historiaSukcesow[K];

    /**
    Generator liczb pseudolosowych
    */
    default_random_engine generator;

    /**
    Uklad formujacy losowe liczby w rozklad normalny
    */
    normal_distribution<double> rozkladNormalny;

    /**
    x1MIN, x1MAX, x2MIN, x2MAX obszar dzialania algorytmu.
    */
    const double X1_MIN;
    const double X1_MAX;
    const double X2_MIN;
    const double X2_MAX;
    const int LICZBA_ITERACJI;
};



#endif
