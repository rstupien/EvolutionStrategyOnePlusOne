#ifndef FUNKCJAPRZYSTOSOWANIA_H
#define FUNKCJAPRZYSTOSOWANIA_H

#include "Chromosom.h"

class FunkcjaPrzystosowania
{
    public:

    /**
    Oblicza formalna funkcje przystosowania zgodna z algorytmem na podstawie chromosomu.
    */
    static double obliczFunkcjePrzystosowania (Chromosom* chromosom);

    /**
    Oblicza funkcje celu naszego problemu optymalizacji.
    */
    static double obliczFunkcjeCelu(double x1, double x2);

};



#endif
