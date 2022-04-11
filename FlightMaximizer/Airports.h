#ifndef AIRPORTS_H
#define AIRPORTS_H
#define _USE_MATH_DEFINES
#include <string>
#include <fstream>
#include <iostream>
#include <sstream>
#include <cmath>

class Airport
{
	std::string IATA;
	long double lattitudeDegs, longitudeDegs, lattitudeRads, longitudeRads;

	void setCoords(std::string IATA)
	{
		std::ifstream inFile("USAirportData.txt");
		std::string line;
		std::string temp;
		while (getline(inFile, line))
		{
			std::istringstream ss(line);
			ss >> temp;
			if (temp == IATA)
			{
				ss >> lattitudeDegs;
				ss >> longitudeDegs;
				break;
			}
		}
	}

public:
	Airport(std::string code) : IATA(code)
	{
		setCoords(this->IATA);
		lattitudeRads = degToRadians(lattitudeDegs);
		longitudeRads = degToRadians(longitudeDegs);
	}

	long double degToRadians(const long double degs)
	{
		long double one_deg = M_PI / 180;
		return (degs * one_deg);
	}

	long double getLatRads() { return lattitudeRads; }
	long double getLatDegs() { return lattitudeDegs; }
	long double getLongRads() { return longitudeRads; }
	long double getLongDegs() { return longitudeDegs; }
	std::string getIATA() { return IATA; }

	
};
#endif //AIRPORTS_H