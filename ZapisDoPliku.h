#ifndef ZAPISDOPLIKU_H
#define ZAPISDOPLIKU_H

#include "chromosom.h"
#include <fstream>

using namespace std;

class ZapisDoPliku
{
    public:

    ZapisDoPliku(char* const nazwaPliku);
    ~ZapisDoPliku();

    /**
    Pisze do strumienia wejsciowego
    */
    void zapiszDoPliku(Chromosom* chromosom);

    private:

    /**
    Zabroniony
    */
    ZapisDoPliku();

    /**
    Zmienna strumieniowa zwiazana z plikiem.
    */
    fstream plik;


};


#endif
