#include "chromosom.h"

class pairChromosomow
{
	public:
		pairChromosomow();
		~pairChromosomow();

		double changeSigma();
		void setParent(chromosom parent);
		void setKid(chromosom kid);
		chromosom getParent();
		chromosom getKid();

	private:
		chromosom parent;
		chromosom kid;
		double sigma;
		static const double C1;
		static const double C2;
};
