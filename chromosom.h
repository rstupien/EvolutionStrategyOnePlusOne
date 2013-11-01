class chromosom
{
	public:
		chromosom();
		~chromosom();

		void setFirstGenotype(double x1);
		void setSecondGenotype(double x2);

		double getFirstGenotype();
		double getSecondGenotype();

	private:
		double x1;
		double x2;
};
