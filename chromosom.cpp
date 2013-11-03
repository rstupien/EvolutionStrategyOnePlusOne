using namespace std;

#include "Chromosom.h"

Chromosom::Chromosom()
{
   this->x1 = 0;
   this->x2 = 0;
}

Chromosom::Chromosom(double x1, double x2)
{
    this->x1 = x1;
    this->x2 = x2;
}

Chromosom::Chromosom(const Chromosom& chromosom)
{
    this->x1 = chromosom.x1;
    this->x2 = chromosom.x2;
}

Chromosom::~Chromosom()
{
    ;
}

double Chromosom::pobierzX1()
{
    return this->x1;
}

double Chromosom::pobierzX2()
{
    return this->x2;
}
