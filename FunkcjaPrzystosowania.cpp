#include "FunkcjaPrzystosowania.h"

#include "Chromosom.h"


double FunkcjaPrzystosowania::obliczFunkcjePrzystosowania (Chromosom* chromosom)
{
    return -1 * obliczFunkcjeCelu(chromosom->pobierzX1(), chromosom->pobierzX2());
}

double FunkcjaPrzystosowania::obliczFunkcjeCelu(double x1, double x2)
{
    return ((x1 + 2*x2 - 7)*(x1 + 2*x2 - 7) + (2*x1 + x2 -5 )*(2*x1 + x2 -5 ));
}
