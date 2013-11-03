#ifndef CHROMOSOM_H
#define CHROMOSOM_H

#include <iostream>

using namespace std;


/**
Klasa przechowuje chromosom skladajacy sie z dwoch genow typu double. Udostepnia medtody pozwalajace pobierac wartosci genow.
*/
class Chromosom
{
    public:

    /**
    Konstruktor bezparametrowy.
    Przypisuje obu skladowym genom chromosomu zerowe wartosci.
    */
    Chromosom();


    /**
    Konstruktor parametrowy.
    Przypisuje obu skladowym genom chromosomu zadane wartosci typu double.
    */
    Chromosom(double tworzonyX1, double tworzonyX2);

    /**
    Konstruktor kopiujacy.
    */
    Chromosom(const Chromosom& chromosom);

    /**
    Destruktor.
    */
    ~Chromosom();

    /**
    Zwraca liczbe typu double bedaca pierwszym genem chromosomu.
    */

    /**
    Zwraca liczbe typu double bedaca pierwszym genem chromosomu.
    */
    double pobierzX1();

    /**
    Zwraca liczbe typu double bedaca pierwszym genem chromosomu.
    */
    double pobierzX2();

    /**
    Przeciazenie operatora =.
    */
    Chromosom& operator= (const Chromosom& chromosomPodstawiany)
    {
        this->x1 = chromosomPodstawiany.x1;
        this->x2 = chromosomPodstawiany.x2;

        return *this;
    }

    friend ostream & operator <<(ostream& wyjscie, const Chromosom& chromosom )
    {
        return wyjscie << chromosom.x1 << " " << chromosom.x2;
    }


    private:

    /**
    Gen o locus nr 1 w chromosomie. Reprezenteuje wartosc pierwszej wspolrzednej na plaszczyznie (x1, x2).
    */
    double x1;

    /**
    Gen o locus nr 2 w chromosomie. Reprezenteuje wartosc drugiej wspolrzednej na plaszczyznie (x1, x2).
    */
    double x2;

};



#endif // CHROMOSOM_H
