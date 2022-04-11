/*#pragma once
#include <fstream>
#include <sstream>
#include <string>
#include <iostream>

using namespace std;


void parseData(ifstream& inFile)
{
	ofstream outfile("output.txt");
	string line;

	while (getline(inFile, line))
	{

		istringstream ss(line);

		string ITCAO, IATA, Airport_Name, City, Country, LatD, LatM, LatS, LongD, LongM, LongS, altitude, Latdec, Longdec, Latdir, Longdir;
		getline(ss, ITCAO, ':');
		getline(ss, IATA, ':');
		if (IATA == "N/A")
			continue;
		getline(ss, Airport_Name, ':');
		getline(ss, City, ':');
		getline(ss, Country, ':');
		if (Country != "USA")
			continue;
		getline(ss, LatD, ':');
		getline(ss, LatM, ':');
		getline(ss, LatS, ':');
		getline(ss, Latdir, ':');
		getline(ss, LongD, ':');
		getline(ss, LongM, ':');
		getline(ss, LongS, ':');
		getline(ss, Longdir, ':');
		getline(ss, altitude, ':');
		getline(ss, Latdec, ':');
		if (Latdec == "0.000")
			continue;
		getline(ss, Longdec, ':');

		//outfile << Airport_Name << ':';
		outfile << IATA << ' ';
		outfile << Latdec << ' ';
		outfile << Longdec << '\n';
		//cout << IATA << ":" << Latdec << ':' << Longdec << '\n';
	}
}*/