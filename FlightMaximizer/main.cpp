#define _USE_MATH_DEFINES
#include <cmath>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include "Airports.h"

using namespace std;

long double distance(Airport& airport1, Airport& airport2)
{
	//d = 3963.0 * acos((sin(lat1) * sin(lat2)) + cos(lat1) * cos(lat2) * cos(long2 - long1));

	long double part1, part2, part3, part4, d, R;
	R = 3963.0;
	part1 = sin(airport1.getLatRads()) * sin(airport2.getLatRads());
	part2 = cos(airport1.getLatRads()) * cos(airport2.getLatRads());
	part3 = cos(airport2.getLongRads() - airport1.getLongRads());
	part4 = part1 + (part2 * part3);
	d = R * acos(part4);
	return d;
}

istream& getline(istream& ins, int& n)
{
	// Read a line (terminated by ENTER|NEWLINE) from the user
	string s;
	if (getline(ins, s))
	{
		// Get rid of any trailing whitespace
		s.erase(s.find_last_not_of(" \f\n\r\t\v") + 1);

		// Convert it to integer
		istringstream ss(s);
		ss >> n;


		// Check to see that there is nothing left over
		if (!ss.eof())
			ins.setstate(std::ios::failbit);
	}
	return ins;
}

bool IsLetter(char in)
{
	return (in >= 'a' && in <= 'z') || (in >= 'A' && in <= 'Z');
}

bool checkCode(const std::string& in)
{
	if (in.size() != 3)
		return false;
	for (uint32_t i = 0; i < in.size(); i++)
		if (!IsLetter(in.at(i)))
			return false;
	return true;
}

int main()
{

	vector<Airport*> airports;
	vector<long double> segments;
	int segs, points;
	long double d, d_total;
	bool valid = false;

	string IATA;
	//Prompt user for airport codes
	cout << "Enter the number of segments: ";
	while (!getline(cin, segs) || segs < 1)
	{
		cin.clear();
		system("CLS");
		cout << "Enter the number of segments: ";
	}

	points = segs + 1;


	for (int i = 0; i < points; i++)
	{
		cout << "Enter the code of Airport " << i + 1 << ": ";
		while (true)
		{
			getline(cin, IATA);

			if (checkCode(IATA))
				break;
			else
				cout << "\x1b[A\r" << "Enter the code of Airport " << i + 1 << ": " << string(20, ' ') << string(20, '\b');
		}
		transform(IATA.begin(), IATA.end(), IATA.begin(), ::toupper);
		airports.emplace_back(new Airport(IATA));
	}

	//Calculate distance
	d_total = 0.0;
	d = 0;
	for (int j = 0; j < segs; j++)
	{
		d = distance(*airports.at(j), *airports.at(j + 1));
		if (segs == 1)
		{
			cout << "The distance from " << airports.at(j)->getIATA() << " to "
				<< airports.at(j + 1)->getIATA() << " is " << d << " miles." << endl;
		}
		else
		{
			cout << "Flight segment " << j + 1 << ": " <<
				airports.at(j)->getIATA() << " to " << airports.at(j + 1)->getIATA()
				<< " is " << d << " miles." << endl;
			d_total += d;
		}
	}
	if (segs > 1)
		cout << "Total distance: " << d_total << " miles." << endl << endl;
}
