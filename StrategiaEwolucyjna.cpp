#include "StrategiaEwolucyjna.h"

#include <chrono>
#include <iostream>
#include <random>
#include "Chromosom.h"
#include "FunkcjaPrzystosowania.h"
#include "ZapisDoPliku.h"

using namespace std;

StrategiaEwolucyjna::StrategiaEwolucyjna(double x10, double x20, double x1Min, double x1Max, double x2Min, double x2Max, int liczbaIteracji) :

    X1_MIN (x1Max>x1Min ? x1Min : x1Max),
    X1_MAX (x1Max>x1Min ? x1Max : x1Min),
    X2_MIN (x2Max>x1Min ? x2Min : x2Max),
    X2_MAX (x2Max>x2Min ? x2Max : x2Min),
    LICZBA_ITERACJI (liczbaIteracji)

{
    double x1 = x10;
    double x2 = x20;

    if (x1 > X1_MAX)
    {
        x1 = X1_MAX;
    }

    if (x1 < X1_MIN)
    {
        x1 = X1_MIN;
    }

    if (x2 > X2_MAX)
    {
        x2 = X2_MAX;
    }

    if (x2 < X1_MIN)
    {
        x2 = X1_MIN;
    }

    this->rodzic = new Chromosom(x1, x2);

    sigma = 1;

    for (int i=0; i<K; i++)
    {
        historiaSukcesow[i] = 0;
    }

    //pobiera bardzo pokretna liczbe do ziarna
    unsigned ziarno = std::chrono::system_clock::now().time_since_epoch().count();
    //inicjuje generator ziarnem
    default_random_engine generator(ziarno);
    //ustawia parametry rozkladu normalnego, wartosc srednia 0, wariancja 1
    normal_distribution<double> rozkladNormalny(0.0,1.0);

}

StrategiaEwolucyjna::~StrategiaEwolucyjna()
{
    delete rodzic;
}

void StrategiaEwolucyjna::start()
{
    ZapisDoPliku plik("ewolucyjny.txt");
    for (int i =0; i<LICZBA_ITERACJI; i++)
    {
    aktualizujHistorieSukcesow(sprawdzCzyZmutowanyJestLepszy(mutuj(rodzic)));
    modyfikujSigme();
    plik.zapiszDoPliku(rodzic);

    }

}

Chromosom* StrategiaEwolucyjna::mutuj(Chromosom* mutowany)
{

    return new Chromosom(mutowany->pobierzX1() + sigma*rozkladNormalny(generator), mutowany->pobierzX2() + sigma*rozkladNormalny(generator) );

}

bool StrategiaEwolucyjna::sprawdzCzyZmutowanyJestLepszy(Chromosom* zmutowany)
{
    //cout << "rodzic " << rodzic->pobierzX1() << ", " << rodzic->pobierzX2() << endl;
    //cout << "zmutowany " << zmutowany->pobierzX1() << ", " << zmutowany->pobierzX2() << endl;
    //cout << "fcja " << FunkcjaPrzystosowania::obliczFunkcjePrzystosowania(*rodzic) << " " << FunkcjaPrzystosowania::obliczFunkcjePrzystosowania(*zmutowany) << endl;

    //jesli nowy punkt wychodzi nam poza zakres poszukiwan, to traktujemy to jako blad.
    if ( zmutowany->pobierzX1() > X1_MAX || zmutowany->pobierzX1() < X1_MIN || zmutowany->pobierzX2() > X2_MAX || zmutowany->pobierzX2() < X2_MIN )
    {
        delete zmutowany;
        return false;
    }

    if (FunkcjaPrzystosowania::obliczFunkcjePrzystosowania(zmutowany) > FunkcjaPrzystosowania::obliczFunkcjePrzystosowania(rodzic))
    {
        delete rodzic;
        rodzic = zmutowany;
        return true;
    }

    else
    {
        delete zmutowany;
        return false;
    }
}

void  StrategiaEwolucyjna::aktualizujHistorieSukcesow(bool czyZmutowanyJestLepszy)
{
    //przesuwamy historie o 1 do tylu
    for (int i = K; i>0; i--)
    {
        historiaSukcesow[i] = historiaSukcesow[i-1];
    }

    historiaSukcesow[0] = czyZmutowanyJestLepszy;

}

void StrategiaEwolucyjna::modyfikujSigme()
{
    double magicznaLiczba = 0.2; // 1/5

    double stosunekSukcesowDoPorazekLicznik = 0;
    double stosunekSukcesowDoPorazekMianownik = (double)K;
    double stosunekSukcesowDoPorazek;

    for (int i = 0; i<K; i++)
    {
        stosunekSukcesowDoPorazekLicznik = (double)historiaSukcesow[i];
    }

    stosunekSukcesowDoPorazek = stosunekSukcesowDoPorazekLicznik/stosunekSukcesowDoPorazekMianownik;

    if (stosunekSukcesowDoPorazek > magicznaLiczba)
    {
        sigma = C2 * sigma;
    }

    if (stosunekSukcesowDoPorazek < magicznaLiczba)
    {
        sigma = C1 * sigma;
    }

    else
    {
        ;
    }

}
