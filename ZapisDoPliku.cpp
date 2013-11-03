#include "ZapisDoPliku.h"

#include <fstream>
#include "FunkcjaPrzystosowania.h"

ZapisDoPliku::ZapisDoPliku(char* const nazwaPliku)
{
     plik.open(nazwaPliku, ios::out);
}


ZapisDoPliku::~ZapisDoPliku()
{
    plik.close();
}

void ZapisDoPliku::zapiszDoPliku (Chromosom* chromosom)
 {
     plik << *chromosom << " " << FunkcjaPrzystosowania::obliczFunkcjeCelu(chromosom->pobierzX1(), chromosom->pobierzX2()) << endl;
 }


