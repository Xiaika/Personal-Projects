#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <limits>
#include "functions.h"

Pixel rotImage[MAX_ROWS][MAX_COLS];
static int rotElevations[MAX_ROWS][MAX_COLS];
int elevations[MAX_ROWS][MAX_COLS];
static Pixel Image[MAX_ROWS][MAX_COLS];

int main()
{
	//Declare variables for user input
	int rows;
	int cols;
	std::string filename;

	//Prompt user to enter rows, columns, and filename, and call validation function for each
	std::cout << "Enter the number of rows: ";
	std::cin >> rows;
	validateInput(rows);
	std::cout << "Enter the number of columns: ";
	std::cin >> cols;
	validateInput(cols);
	std::cout << "Enter the full filename: ";
	std::cin >> filename;
	//Test that the file opens successfully and if it does, set its final name to the result
	filename = validateInput(filename);

	//Mock file stream to make sure there are no errors in the input file
	std::ifstream verifyInData(filename);
	validateInput(rows, cols, verifyInData);
	
	//Actual file stream for input data file
	std::fstream inData(filename);
	//Load our array with values, (see function definition)
	loadData(elevations, rows, cols, inData);

	//Create min max variables and initialize
	int max = 0;
	int min = 0;
	//Change max and min by reference when a new max or min is found
	findMaxMin(elevations, rows, cols, max, min);

	//Load our Image array with grey values for Red green and blue (see definition)
	loadGreyscale(Image, elevations, rows, cols, max, min);

	//Create red color 
	Pixel colorRed;
	colorRed.red = 252;
	colorRed.green = 25;
	colorRed.blue = 63;

	//Create Green color
	Pixel colorGreen;
	colorGreen.red = 31;
	colorGreen.green = 253;
	colorGreen.blue = 13;

	//Create aqua color
	Pixel colorAqua;
	colorAqua.red = 19;
	colorAqua.green = 254;
	colorAqua.blue = 253;

	int distance;
	//Create and initialize a temp variable to determine shortest path
	int tempShortestPath = 0;
	//Varibale to represent the final shortest path
	int shortestPath;
	//Iterate through all rows in the elevations array
	for (int start_row = 0; start_row < rows; start_row++)
	{
		//Initialize distance of the path to zero each time we loop
		distance = 0;
		//Accumulate a total distance based on the returned value of colorPath
		distance += colorPath(elevations, Image, rows, cols, colorRed, start_row, 0);
		//If we are at the first row then our temp variable is simply = to distance (0)
		if(start_row == 0)
			tempShortestPath = distance;

		//Otherwise our temp variable will chance if the sum of returned distances is less than the temp
		if (distance < tempShortestPath)
		{
			tempShortestPath = distance;
			//Shortest path starts at start row
			shortestPath = start_row;
		}
	}
	std::cout << "Row: " << shortestPath << " Distance: " << tempShortestPath;

	//run Color paaths once more on the shortest path and color it green
	colorPath(elevations, Image, rows, cols, colorGreen, shortestPath, 0);

	int start_row = 164;
	int start_col = 388;
	

	
	for (int rotate = 0; rotate < 4; rotate++)
	{
		if (rotate == 0)
			colorPath(elevations, Image, rows, cols, colorAqua, start_row, start_col);
		for (int y = 0; y < cols; y++)
		{
			for (int x = 0; x < rows; x++)
			{
				rotImage[x][y] = Image[rows - 1 - x][y];
				rotElevations[x][y] = elevations[rows - 1 - x][y];
				if(rotate != 3)
					colorPath(rotElevations, rotImage, rows, cols, colorAqua, start_row, start_col);
			}
		}
	}

	//Append .ppm to the filename for the final output file
	std::string outfile_name = filename + ".ppm";

	//Create an ostream using our ppm output file for all of our pixel colors
	std::ofstream outData(outfile_name);
	if (!outData.is_open())
		std::cout << "Error: could not open PPM file.";
	//Output the Image array to the PPM file
	outputImage(rotImage, rows, cols, outData);
	outData.close();
}