#include <iostream>

#include "StrategiaEwolucyjna.h"

#include <chrono>
#include <random>
using namespace std;

int main()
{
   StrategiaEwolucyjna str(5,5,-5,5,-5,5,1000);
   str.start();

}
