#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <iostream>
#include <fstream>
#include <string>

const int MAX_ROWS = 1000;
const int MAX_COLS = 1000;


class Pixel {
public:
	int red;
	int green;
	int blue;

};


int colorPath(const int elevations[MAX_ROWS][MAX_COLS], Pixel image[MAX_ROWS][MAX_COLS], int rows, int cols, Pixel color, int start_row, int start_col);

void findMaxMin(const int elevations[MAX_ROWS][MAX_COLS], int rows, int cols, int &max, int &min);

void loadData(int elevations[MAX_ROWS][MAX_COLS], int rows, int cols, std::istream &inData);

void loadGreyscale(Pixel Image[MAX_ROWS][MAX_COLS], const int elevations[MAX_ROWS][MAX_COLS], int rows, int cols, int max, int min);

void outputImage(Pixel image[MAX_ROWS][MAX_COLS], int rows, int cols, std::ostream &outData);

int scaleValue(int value, int max, int min);

int validateInput(int number);

int validateInput(int rows, int cols, std::istream &inData);

std::string validateInput(std::string filename);


#endif
